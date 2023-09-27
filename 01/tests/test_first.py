import unittest
from unittest import mock

from src.first_predict_message import predict_message_mood, LogicError
from src.first_model import SomeModel


class TestFirst(unittest.TestCase):
    def setUp(self):
        self.m = SomeModel()

    def test_good_threshold_default(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.80001
            expected_calls = [mock.call("message_g")]

            self.assertEqual("отл", predict_message_mood("message_g", self.m))
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_good_threshold_set(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.8

            self.assertEqual("отл", predict_message_mood("message_g",
                                                         self.m,
                                                         good_thresholds=0.79))
            self.assertEqual("отл", predict_message_mood("message_g",
                                                         self.m,
                                                         0.1,
                                                         0.79))

            expected_calls = [mock.call("message_g"),
                              mock.call("message_g")]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_bad_threshold_default(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.29
            expected_calls = [mock.call("message_b")]

            self.assertEqual("неуд", predict_message_mood("message_b", self.m))
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_bad_threshold_set(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.28
            self.assertEqual("неуд", predict_message_mood("message_b",
                                                          self.m,
                                                          bad_thresholds=0.29))

            mock_predict.return_value = -101
            self.assertEqual("неуд", predict_message_mood("message_b",
                                                          self.m,
                                                          bad_thresholds=-100))
            self.assertEqual("неуд", predict_message_mood("message_b",
                                                          self.m,
                                                          -100, 0))

            expected_calls = [mock.call("message_b"),
                              mock.call("message_b"),
                              mock.call("message_b")]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_neutral_result_default(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.3
            self.assertEqual("норм", predict_message_mood("message_n", self.m))

            mock_predict.return_value = 0.8
            self.assertEqual("норм", predict_message_mood("message_n", self.m))

            mock_predict.return_value = 0.5
            self.assertEqual("норм", predict_message_mood("message_n", self.m))

            expected_calls = [mock.call("message_n"),
                              mock.call("message_n"),
                              mock.call("message_n")]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_neutral_result_set(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.2
            self.assertEqual("норм", predict_message_mood("message_n",
                                                          self.m,
                                                          0.19, 0.21))

            mock_predict.return_value = 0
            self.assertEqual("норм", predict_message_mood("message_n",
                                                          self.m,
                                                          -100, 100))

            mock_predict.return_value = -100
            self.assertEqual("норм", predict_message_mood("message_n",
                                                          self.m,
                                                          -100, 100))

            mock_predict.return_value = 100
            self.assertEqual("норм", predict_message_mood("message_n",
                                                          self.m,
                                                          -100, 100))

            expected_calls = [mock.call("message_n"),
                              mock.call("message_n"),
                              mock.call("message_n"),
                              mock.call("message_n")]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_message_transmission(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.5
            self.assertEqual("норм", predict_message_mood("message_1", self.m))
            self.assertEqual("норм", predict_message_mood("message_2", self.m))
            self.assertEqual("норм", predict_message_mood("message_3", self.m))

            expected_calls = [mock.call("message_1"),
                              mock.call("message_2"),
                              mock.call("message_3")]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_message_incorrect_type(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            with self.assertRaises(TypeError):
                predict_message_mood(1, self.m)
            expected_calls = []
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_model_incorrect_type(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            with self.assertRaises(TypeError):
                predict_message_mood("message", 1)
            expected_calls = []
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_bad_th_incorrect_type(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            with self.assertRaises(TypeError):
                predict_message_mood("message", self.m, bad_thresholds="")
            with self.assertRaises(TypeError):
                predict_message_mood("message", self.m, "")
            expected_calls = []
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_good_th_incorrect_type(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            with self.assertRaises(TypeError):
                predict_message_mood("message", self.m, good_thresholds={})
            expected_calls = []
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_logic_thresholds(self):
        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.5

            with self.assertRaises(LogicError):
                predict_message_mood("message", self.m, 10, -10)
            with self.assertRaises(LogicError):
                predict_message_mood("message", self.m, 1, 1)
            expected_calls = []
            self.assertEqual(expected_calls, mock_predict.mock_calls)

            self.assertEqual("норм", predict_message_mood("message",
                                                          self.m,
                                                          0, 1))
            self.assertEqual("норм", predict_message_mood("message", self.m))
            expected_calls = [mock.call("message"),
                              mock.call("message")]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_model_hassattr(self):
        self.assertTrue(hasattr(self.m, "predict"))

        mock_m = mock.MagicMock(self.m)
        delattr(mock_m, "predict")

        with mock.patch("src.first_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.5

            with self.assertRaises(AttributeError):
                predict_message_mood("message", mock_m)

        expected_calls = []
        self.assertEqual(expected_calls, mock_predict.mock_calls)
