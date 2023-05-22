#!/usr/bin/env python3


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, patch):

        patch.return_value =        expected
        x = GithubOrgClient(org_name)
        self.assertEqual(x.org_name, expected)
        patch.assert_called_once_with("https://api.github.com/orgs/"+org_name)