import pytest

from src.custom_list import CustomList


class TestInit:
    def test_init_correct(self):
        c1 = CustomList()
        c2 = CustomList([1, 2, 3])
        c3 = CustomList(None)

        assert c1.lst == []
        assert c2.lst == [1, 2, 3]
        assert c3.lst == []

    def test_init_wrong_type(self):
        with pytest.raises(TypeError):
            CustomList(1)
        with pytest.raises(TypeError):
            CustomList({1, 2, 3})


class TestLen:
    def test_len(self):
        c1 = CustomList()
        c2 = CustomList([1, 2, 3])
        c3 = CustomList(None)

        assert len(c1) == 0
        assert len(c2) == 3
        assert len(c3) == 0


class TestGetItem:
    def test_incorrect_getitem(self):
        c = CustomList([1, 2, 3])

        with pytest.raises(TypeError):
            c['a': 'b': 'c']
        with pytest.raises(IndexError):
            c[1: 4: 1]
        with pytest.raises(TypeError):
            c[1:: 3.0]
        with pytest.raises(TypeError):
            c['a']
        with pytest.raises(IndexError):
            c[-4]

    def test_correct_getitem(self):
        c = CustomList([1, 2, 3])

        assert c[0] == 1
        assert c[-1] == 3
        assert c[0:] == [1, 2, 3]
        assert c[:1] == [1]
        assert c[::2] == [1, 3]
        assert c[0:2:1] == [1, 2]


class TestPlus:
    def test_add_list_equal(self):
        c1 = CustomList([1, 2, 3])
        c2 = [1, 2, 3]
        res = c1 + c2

        assert isinstance(res, CustomList)
        assert res.lst == [2, 4, 6]
        assert c1.lst == [1, 2, 3]
        assert c2 == [1, 2, 3]

    def test_add_list_greater(self):
        c1 = CustomList([1, 2])
        c2 = [1, 2, 3]
        res = c1 + c2

        assert isinstance(res, CustomList)
        assert res.lst == [2, 4, 3]
        assert c1.lst == [1, 2]
        assert c2 == [1, 2, 3]

    def test_add_list_less(self):
        c1 = CustomList([1, 2, 6])
        c2 = [1, 2]
        res = c1 + c2

        assert isinstance(res, CustomList)
        assert res.lst == [2, 4, 6]
        assert c1.lst == [1, 2, 6]
        assert c2 == [1, 2]

    def test_add_customlist_equal(self):
        c1 = CustomList([1, 2, 3])
        c2 = CustomList([3, 4, 5])
        res = c1 + c2

        assert isinstance(res, CustomList)
        assert res.lst == [4, 6, 8]
        assert c1.lst == [1, 2, 3]
        assert c2.lst == [3, 4, 5]

    def test_add_customlist_greater(self):
        c1 = CustomList([1, 2, 3])
        c2 = CustomList([3, 4])
        res = c1 + c2

        assert isinstance(res, CustomList)
        assert res.lst == [4, 6, 3]
        assert c1.lst == [1, 2, 3]
        assert c2.lst == [3, 4]

    def test_add_customlist_less(self):
        c1 = CustomList([1, 2])
        c2 = CustomList([3, 4, 5, 5])
        res = c1 + c2

        assert isinstance(res, CustomList)
        assert res.lst == [4, 6, 5, 5]
        assert c1.lst == [1, 2]
        assert c2.lst == [3, 4, 5, 5]

    def test_radd_equal(self):
        c1 = [1, 2, 4]
        c2 = CustomList([3, 4, 5])
        res = c1 + c2

        assert isinstance(res, CustomList)
        assert res.lst == [4, 6, 9]
        assert c1 == [1, 2, 4]
        assert c2.lst == [3, 4, 5]

    def test_radd_less(self):
        c1 = [1, 2]
        c2 = CustomList([3, 4, 5])
        res = c1 + c2

        assert isinstance(res, CustomList)
        assert res.lst == [4, 6, 5]
        assert c1 == [1, 2]
        assert c2.lst == [3, 4, 5]

    def test_radd_greater(self):
        c1 = [1, 2, 5, 7]
        c2 = CustomList([3, 4, 5])
        res = c1 + c2

        assert isinstance(res, CustomList)
        assert res.lst == [4, 6, 10, 7]
        assert c1 == [1, 2, 5, 7]
        assert c2.lst == [3, 4, 5]


class TestMinus:
    def test_sub_list_equal(self):
        c1 = CustomList([1, 2, 3])
        c2 = [1, 2, 3]
        res = c1 - c2

        assert isinstance(res, CustomList)
        assert res.lst == [0, 0, 0]
        assert c1.lst == [1, 2, 3]
        assert c2 == [1, 2, 3]

    def test_sub_list_greater(self):
        c1 = CustomList([2, 2])
        c2 = [1, 2, 3]
        res = c1 - c2

        assert isinstance(res, CustomList)
        assert res.lst == [1, 0, -3]
        assert c1.lst == [2, 2]
        assert c2 == [1, 2, 3]

    def test_sub_list_less(self):
        c1 = CustomList([3, 3, 6])
        c2 = [1, 2]
        res = c1 - c2

        assert isinstance(res, CustomList)
        assert res.lst == [2, 1, 6]
        assert c1.lst == [3, 3, 6]
        assert c2 == [1, 2]

    def test_sub_customlist_equal(self):
        c1 = CustomList([1, 2, 3])
        c2 = CustomList([3, 4, 5])
        res = c1 - c2

        assert isinstance(res, CustomList)
        assert res.lst == [-2, -2, -2]
        assert c1.lst == [1, 2, 3]
        assert c2.lst == [3, 4, 5]

    def test_sub_customlist_greater(self):
        c1 = CustomList([1, 2, 3])
        c2 = CustomList([3, 4])
        res = c1 - c2

        assert isinstance(res, CustomList)
        assert res.lst == [-2, -2, 3]
        assert c1.lst == [1, 2, 3]
        assert c2.lst == [3, 4]

    def test_sub_customlist_less(self):
        c1 = CustomList([1, 2])
        c2 = CustomList([3, 4, 5, 5])
        res = c1 - c2

        assert isinstance(res, CustomList)
        assert res.lst == [-2, -2, -5, -5]
        assert c1.lst == [1, 2]
        assert c2.lst == [3, 4, 5, 5]

    def test_rsub_equal(self):
        c1 = [1, 2, 4]
        c2 = CustomList([3, 4, 5])
        res = c1 - c2

        assert isinstance(res, CustomList)
        assert res.lst == [-2, -2, -1]
        assert c1 == [1, 2, 4]
        assert c2.lst == [3, 4, 5]

    def test_rsub_less(self):
        c1 = [1, 2]
        c2 = CustomList([3, 4, 5])
        res = c1 - c2

        assert isinstance(res, CustomList)
        assert res.lst == [-2, -2, -5]
        assert c1 == [1, 2]
        assert c2.lst == [3, 4, 5]

    def test_rsub_greater(self):
        c1 = [1, 2, 5, 7]
        c2 = CustomList([3, 4, 5])
        res = c1 - c2

        assert isinstance(res, CustomList)
        assert res.lst == [-2, -2, 0, 7]
        assert c1 == [1, 2, 5, 7]
        assert c2.lst == [3, 4, 5]


class TestEqualLessGreater:
    def test_eq(self):
        c1 = CustomList([3, 4, 5])
        c2 = CustomList([4, 8])
        c3 = CustomList([1, 2, 3])

        assert c1 == c2
        assert not c1 == c3

    def test_ne(self):
        c1 = CustomList([3, 4, 5])
        c2 = CustomList([4, 8])
        c3 = CustomList([1, 2, 3])

        assert c1 != c3
        assert not c1 != c2

    def test_ge(self):
        c1 = CustomList([3, 4, 5])
        c2 = CustomList([4, 8])
        c3 = CustomList([1, 2, 13])

        assert c1 >= c2
        assert not c2 >= c3
        assert c3 >= c2

    def test_gt(self):
        c1 = CustomList([3, 4, 5])
        c2 = CustomList([4, 8])
        c3 = CustomList([1, 2, 13])

        assert not c1 > c2
        assert not c2 > c3
        assert c3 > c2

    def test_le(self):
        c1 = CustomList([3, 4, 5])
        c2 = CustomList([4, 8])
        c3 = CustomList([1, 2, 13])

        assert c1 <= c2
        assert c2 <= c3
        assert not c3 <= c2

    def test_lt(self):
        c1 = CustomList([3, 4, 5])
        c2 = CustomList([4, 8])
        c3 = CustomList([1, 2, 13])

        assert not c1 < c2
        assert c2 < c3
        assert not c3 < c2


class TestString:
    def test_str(self):
        c1 = CustomList([3, 4, 5])
        c2 = CustomList()

        assert str(c1) == "3 4 5 \nsum = 12"
        assert str(c2) == "\nsum = 0"
