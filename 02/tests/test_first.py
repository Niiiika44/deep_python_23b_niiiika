from json.decoder import JSONDecodeError
import unittest
from unittest import mock

from src.first_json_callback import parse_json


class TestFirst(unittest.TestCase):
    def test_json_type(self):
        with self.assertRaises(TypeError):
            parse_json({"key1": "value1"},
                       ["key1"],
                       ["value1"])
        with self.assertRaises(JSONDecodeError):
            parse_json("key1: value1",
                       ["key1"],
                       ["value1"])

        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = [mock.call("key2", "word3")]
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       ["key1", "key2"],
                       ["word3"],
                       mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_keywords_type(self):
        with self.assertRaises(TypeError):
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       ["key1", "key2"],
                       ("word3"))

        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = [mock.call("key2", "word3")]
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       ["key1", "key2"],
                       ["word3"],
                       mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_required_fields_type(self):
        with self.assertRaises(TypeError):
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       ("key1", "key2"),
                       ["word3"])

        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = [mock.call("key2", "word3")]
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       ["key1", "key2"],
                       ["word3"],
                       mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_callback_type(self):
        with self.assertRaises(TypeError):
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       ["key1", "key2"],
                       ["word3"],
                       'not a func')

        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = [mock.call("key2", "word3")]
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       ["key1", "key2"],
                       ["word3"],
                       mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_missing_fields(self):
        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = []
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       [],
                       ["word3"],
                       mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_missing_keywords(self):
        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = []
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       ["key1", "key2"],
                       [],
                       mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_default_fields(self):
        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = []
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       keywords=["word3"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_default_keywords(self):
        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = []
            parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                       required_fields=["key1", "key2"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_multiple(self):
        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = [mock.call("key1", "word1"),
                              mock.call("key1", "word2"),
                              mock.call("key2", "word2")]
            parse_json('{"key1": "word1 word2", "key2": "word2 word3"}',
                       required_fields=["key1", "key2"],
                       keywords=["word1", "word2"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_case_sensitive_fields(self):
        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = [mock.call("key2", "word2")]
            parse_json('{"Key1": "word1 word2", "key2": "word2 word3"}',
                       required_fields=["key1", "key2"],
                       keywords=["word2"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_case_insensitive_keywords(self):
        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = [mock.call("key1", "word2"),
                              mock.call("key1", "worD1")]
            parse_json('{"key1": "worD1 word2", "key2": "word2 word3"}',
                       required_fields=["key1"],
                       keywords=["WorD2", "WORD1"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_nonmatching_fields(self):
        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = []
            parse_json('{"key1": "word1 word2", "key2": "word2 word3"}',
                       required_fields=["key3"],
                       keywords=["word2", "word1"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_nonmatching_keywords(self):
        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = []
            parse_json('{"key1": "word1 word2", "key2": "word2 word3"}',
                       required_fields=["key1"],
                       keywords=["word4", "word5"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_keywords_separation(self):
        with mock.patch("src.first_json_callback.keyword_callback")\
             as mock_callback:
            expected_calls = []
            parse_json('{"key1": "word1extra word2", "key2": "word2 word3"}',
                       required_fields=["key1"],
                       keywords=["word1"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

            expected_calls = [mock.call("key1", "word1")]
            parse_json('{"key1": "word1 word2", "key2": "word2 word3"}',
                       required_fields=["key1"],
                       keywords=["word1"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

            expected_calls.append(mock.call("key1", "word1"))
            parse_json('{"key1": "word1|word2", "key2": "word2 word3"}',
                       required_fields=["key1"],
                       keywords=["word1"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

            expected_calls.append(mock.call("key1", "word1"))
            parse_json('{"key1": "word1;word2", "key2": "word2 word3"}',
                       required_fields=["key1"],
                       keywords=["word1"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)

            expected_calls.append(mock.call("key1", "word1"))
            parse_json('{"key1": "word1,word2", "key2": "word2 word3"}',
                       required_fields=["key1"],
                       keywords=["word1"],
                       callback=mock_callback)
            self.assertEqual(expected_calls, mock_callback.mock_calls)
