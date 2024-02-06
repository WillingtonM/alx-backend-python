#!/usr/bin/env python3
"""
Module: for testing the client module
"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
        Tests GithubOrgClient class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """
            Test TestGithubOrgClient.org method
        """
        tst_cls = GithubOrgClient(org_name)
        tst_cls.org()
        mock.called_with_once(tst_cls.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """
            Tests _public_repos_url property
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            pay_load = {"repos_url": "something"}
            mock.return_value = pay_load
            tst_cls = GithubOrgClient('test')
            res = tst_cls._public_repos_url
            self.assertEqual(res, pay_load["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
            Tests public_repos method
            returns correct value
        """
        pay_loads = [{"name": "google"}, {"name": "Twitter"}]
        mock_json.return_value = pay_loads

        with patch('client.GithubOrgClient._public_repos_url') as mock_pblc:
            mock_pblc.return_value = "hey there!"
            tst_cls = GithubOrgClient('test')
            res = tst_cls.public_repos()

            expctd = [p["name"] for p in pay_loads]
            self.assertEqual(res, expctd)

            mock_json.called_with_once()
            mock_pblc.called_with_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
            Tests has_license method
        """
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
        Performs integration tests for GithubOrgClient class
    """
    @classmethod
    def setUpClass(cls):
        """
            Setsup class fixtures before running the tests
        """
        conf = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}

        cls.get_patcher = patch('requests.get', **conf)
        cls.mock = cls.get_patcher.start()

    def test_public_repo(self):
        """
            Tests public_repos method
        """
        tst_cls = GithubOrgClient('Google')

        self.assertEqual(tst_cls.org, self.org_payload)
        self.assertEqual(tst_cls.repos_payload, self.repos_payload)
        self.assertEqual(tst_cls.public_repos(), self.expected_repos)
        self.assertEqual(tst_cls.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """
            Tests public_repos method with license
        """
        tst_cls = GithubOrgClient("google")

        self.assertEqual(tst_cls.public_repos(), self.expected_repos)
        self.assertEqual(tst_cls.public_repos("XLICENSE"), [])
        self.assertEqual(tst_cls.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """
            Removes class fixtures after running all tests
        """
        cls.get_patcher.stop()
