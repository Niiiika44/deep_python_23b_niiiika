import unittest

from src.second_generator import gen


class TestFirst(unittest.TestCase):
    def setUp(self):
        self.filename = r"src\second_text.txt"
        self.f = open(self.filename, encoding="utf-8")

    def tearDown(self):
        self.f.close()

    def test_type_words(self):
        with self.assertRaises(TypeError):
            g = gen(self.filename, {"душа", "была"})
            while True:
                next(g)

        g = gen(self.filename, ["душа", "была"])
        self.assertEqual(next(g), "вот бы у меня была душа")
        self.assertEqual(next(g), "душа душа душа")
        self.assertEqual(next(g), "ДуШа моя неспокойна")

        with self.assertRaises(StopIteration):
            next(g)

    def test_len_words(self):
        with self.assertRaises(ValueError):
            g = gen(self.filename, [])
            while True:
                next(g)

        g = gen(self.filename, ["дз"])
        self.assertEqual(next(g), "в это дз я вложила свою душу")
        with self.assertRaises(StopIteration):
            next(g)

    def test_str_words(self):
        with self.assertRaises(ValueError):
            g = gen(self.filename, [2, 2, 8])
            while True:
                next(g)

        g = gen(self.filename, ["дз"])
        self.assertEqual(next(g), "в это дз я вложила свою душу")
        with self.assertRaises(StopIteration):
            next(g)

    def test_filetype(self):
        with self.assertRaises(ValueError):
            g = gen(["it`s definitely not a file"], ["дз"])
            while True:
                next(g)

        g = gen(self.filename, ["дз"])
        self.assertEqual(next(g), "в это дз я вложила свою душу")
        with self.assertRaises(StopIteration):
            next(g)

        g = gen(self.f, ["дз"])
        self.assertEqual(next(g), "в это дз я вложила свою душу")
        with self.assertRaises(StopIteration):
            next(g)

    def test_file_isclosed(self):
        g = gen(self.f, ["дз"])
        self.assertEqual(next(g), "в это дз я вложила свою душу")
        with self.assertRaises(StopIteration):
            next(g)
        self.assertTrue(self.f.closed)

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            g = gen("src/not-a-real-file.txt", ["дз"])
            while True:
                next(g)

        g = gen(self.filename, ["дз"])
        self.assertEqual(next(g), "в это дз я вложила свою душу")
        with self.assertRaises(StopIteration):
            next(g)

    def test_uppercase_words(self):
        g = gen(self.filename, ["ДуШанБЕ"])
        self.assertEqual(next(g), "а может душаНБЕ")
        with self.assertRaises(StopIteration):
            next(g)

    def test_empty_file(self):
        filename = "src/second_empty_text.txt"
        g = gen(filename, ["дз"])
        with self.assertRaises(StopIteration):
            next(g)

        f = open(filename, encoding="utf-8")
        g = gen(f, ["дз"])
        with self.assertRaises(StopIteration):
            next(g)

        self.assertTrue(f.closed)

    def test_unmatched_words(self):
        g = gen(self.filename, ["мечта"])
        with self.assertRaises(StopIteration):
            next(g)

        g = gen(self.f, ["мечта", "надежда"])
        with self.assertRaises(StopIteration):
            next(g)
        self.assertTrue(self.f.closed)
