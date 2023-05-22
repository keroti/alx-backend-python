#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""
import unittest
from typing import Mapping, Sequence, Any, Dict
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


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
