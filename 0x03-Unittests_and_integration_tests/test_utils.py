#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""
import unittest
from typing import Mapping, Sequence, Any, Dict
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected_result: Any
    ) -> None:
        """
        Test the access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """
        Test that a KeyError is raised when accessing a non-existing key
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(
        self, test_url: str, test_payload: Dict, mock_get: Mock
    ) -> None:
        """
        Test the get_json function to return correct output
        """
        mock_get.return_value.json.return_value = test_payload
        response = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class that inherits from unittest.TestCase.
    """

    def test_memoize(self):
        """
        Test the memoize function.
        """
        class TestClass:
            """
            TestClass with a_method and a_property
            and return 42.
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()
            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
