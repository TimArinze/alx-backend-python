#!/usr/bin/env python3
"""
Parameterize a unit test
"""
from parameterized import parameterized
import unittest
import utils
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """Testing access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Testing get_json function"""
    test_data = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
            ]
    @parameterized.expand(test_data)
    @patch('utils.requests.get')
    def test_get_json(self, mock_request, test_url, test_payload):
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_request.return_value = mock_response
        self.assertEqual(utils.get_json(test_url), test_payload)


if __name__ == "__main__":
    unittest.main()
