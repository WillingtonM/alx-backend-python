#!/usr/bin/env python3
"""
    Unittest Test Parameterize
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch

from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """
        nested map test method
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as errs:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(errs.exception))


class TestGetJson(unittest.TestCase):
    """
        get json unittest Class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
            Test get json utils function
        """
        conf = {'return_value.json.return_value': test_payload}
        ptch = patch('requests.get', **conf)
        mock = ptch.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        ptch.stop()


class TestMemoize(unittest.TestCase):
    """
        Memoiize test class
    """

    def test_memoize(self):
        """
            Test memoize method
        """

        class TestClass:
            """
                class wrapper for memoize method
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
