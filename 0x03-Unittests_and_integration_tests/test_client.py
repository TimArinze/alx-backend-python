#!/usr/bin/env python3
"""
Parameterize and patch as decorator
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, MagicMock
import client


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient"""
    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"})
        ])
    def test_org(self, test_endpoint, org_dict):
        """testing org method"""
        with patch('client.get_json') as mock_get_json:
            mock_response = MagicMock()
            mock_response.json.return_value = org_dict
            mock_response.return_value = mock_response
            testClass = client.GithubOrgClient(test_endpoint)
            self.assertEqual(testClass._org_name, org_dict["org"])
            #mock_get_json.assert_called_once_with(client.GithubOrgClient(test_endpoint).ORG_URL.format(org=test_endpoint))


if __name__ == "__main__":
    unittest.main()
