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
    def test_get_json(self, test_url, test_payload):
        with patch('utils.requests') as mock_request:
            mock_response = MagicMock()
            mock_response.json.return_value = test_payload
            mock_request.get.return_value = mock_response
            self.assertEqual(utils.get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Testing memoizing function wrap"""
    def test_memoize(self):
        """Test that will test the caching ability of the memoize"""


        class TestClass:
            """TestClass"""
            def a_method(self):
                """a_method"""
                return 42

            @utils.memoize
            def a_property(self):
                """a_property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
