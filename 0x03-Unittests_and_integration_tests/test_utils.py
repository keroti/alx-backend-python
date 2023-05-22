#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""
import unittest
from typing import Mapping, Sequence, Any
from parameterized import parameterized
from utils import access_nested_map


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

        Parameters:
            nested_map (Mapping)
            path: A sequence of keys
            representing a path to the value.
            expected_result (Any): The expected result.

        Returns:
            None.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence
    ) -> None:
        """
        Test that a KeyError is raised when accessing a non-existing key.

        Parameters:
            nested_map (Mapping)
            path: A sequence of keys representing a path to the value.

        Returns:
            None.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), "Key not found in nested map")
