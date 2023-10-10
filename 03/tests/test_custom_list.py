import pytest

from src.custom_list import CustomList


def test_init_correct():
    c1 = CustomList()
    c2 = CustomList([1, 2, 3])
    c3 = CustomList(None)

    assert c1.lst == []
    assert c2.lst == [1, 2, 3]
    assert c3.lst == []


def test_init_wront_type():
    with pytest.raises(TypeError):
        CustomList(1)
    with pytest.raises(TypeError):
        CustomList({1, 2, 3})


def test_len():
    c1 = CustomList()
    c2 = CustomList([1, 2, 3])
    c3 = CustomList(None)

    assert len(c1) == 0
    assert len(c2) == 3
    assert len(c3) == 0


def test_incorrect_getitem():
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


def test_correct_getitem():
    c = CustomList([1, 2, 3])

    assert c[0] == 1
    assert c[-1] == 3
    assert c[0:] == [1, 2, 3]
    assert c[:1] == [1]
    assert c[::2] == [1, 3]
    assert c[0:2:1] == [1, 2]


def test_add_list_equal():
    c1 = CustomList([1, 2, 3])
    c2 = [1, 2, 3]
    res = c1 + c2

    assert isinstance(res, CustomList)
    assert res.lst == [2, 4, 6]
    assert c1.lst == [1, 2, 3]
    assert c2 == [1, 2, 3]


def test_add_list_greater():
    c1 = CustomList([1, 2])
    c2 = [1, 2, 3]
    res = c1 + c2

    assert isinstance(res, CustomList)
    assert res.lst == [2, 4, 3]
    assert c1.lst == [1, 2]
    assert c2 == [1, 2, 3]


def test_add_list_less():
    c1 = CustomList([1, 2, 6])
    c2 = [1, 2]
    res = c1 + c2

    assert isinstance(res, CustomList)
    assert res.lst == [2, 4, 6]
    assert c1.lst == [1, 2, 6]
    assert c2 == [1, 2]


def test_add_customlist_equal():
    c1 = CustomList([1, 2, 3])
    c2 = CustomList([3, 4, 5])
    res = c1 + c2

    assert isinstance(res, CustomList)
    assert res.lst == [4, 6, 8]
    assert c1.lst == [1, 2, 3]
    assert c2.lst == [3, 4, 5]


def test_add_customlist_greater():
    c1 = CustomList([1, 2, 3])
    c2 = CustomList([3, 4])
    res = c1 + c2

    assert isinstance(res, CustomList)
    assert res.lst == [4, 6, 3]
    assert c1.lst == [1, 2, 3]
    assert c2.lst == [3, 4]


def test_add_customlist_less():
    c1 = CustomList([1, 2])
    c2 = CustomList([3, 4, 5, 5])
    res = c1 + c2

    assert isinstance(res, CustomList)
    assert res.lst == [4, 6, 5, 5]
    assert c1.lst == [1, 2]
    assert c2.lst == [3, 4, 5, 5]


def test_radd_equal():
    c1 = [1, 2, 4]
    c2 = CustomList([3, 4, 5])
    res = c1 + c2

    assert isinstance(res, CustomList)
    assert res.lst == [4, 6, 9]
    assert c1 == [1, 2, 4]
    assert c2.lst == [3, 4, 5]


def test_radd_less():
    c1 = [1, 2]
    c2 = CustomList([3, 4, 5])
    res = c1 + c2

    assert isinstance(res, CustomList)
    assert res.lst == [4, 6, 5]
    assert c1 == [1, 2]
    assert c2.lst == [3, 4, 5]


def test_radd_greater():
    c1 = [1, 2, 5, 7]
    c2 = CustomList([3, 4, 5])
    res = c1 + c2

    assert isinstance(res, CustomList)
    assert res.lst == [4, 6, 10, 7]
    assert c1 == [1, 2, 5, 7]
    assert c2.lst == [3, 4, 5]


def test_sub_list_equal():
    c1 = CustomList([1, 2, 3])
    c2 = [1, 2, 3]
    res = c1 - c2

    assert isinstance(res, CustomList)
    assert res.lst == [0, 0, 0]
    assert c1.lst == [1, 2, 3]
    assert c2 == [1, 2, 3]


def test_sub_list_greater():
    c1 = CustomList([2, 2])
    c2 = [1, 2, 3]
    res = c1 - c2

    assert isinstance(res, CustomList)
    assert res.lst == [1, 0, -3]
    assert c1.lst == [2, 2]
    assert c2 == [1, 2, 3]


def test_sub_list_less():
    c1 = CustomList([3, 3, 6])
    c2 = [1, 2]
    res = c1 - c2

    assert isinstance(res, CustomList)
    assert res.lst == [2, 1, 6]
    assert c1.lst == [3, 3, 6]
    assert c2 == [1, 2]


def test_sub_customlist_equal():
    c1 = CustomList([1, 2, 3])
    c2 = CustomList([3, 4, 5])
    res = c1 - c2

    assert isinstance(res, CustomList)
    assert res.lst == [-2, -2, -2]
    assert c1.lst == [1, 2, 3]
    assert c2.lst == [3, 4, 5]


def test_sub_customlist_greater():
    c1 = CustomList([1, 2, 3])
    c2 = CustomList([3, 4])
    res = c1 - c2

    assert isinstance(res, CustomList)
    assert res.lst == [-2, -2, 3]
    assert c1.lst == [1, 2, 3]
    assert c2.lst == [3, 4]


def test_sub_customlist_less():
    c1 = CustomList([1, 2])
    c2 = CustomList([3, 4, 5, 5])
    res = c1 - c2

    assert isinstance(res, CustomList)
    assert res.lst == [-2, -2, -5, -5]
    assert c1.lst == [1, 2]
    assert c2.lst == [3, 4, 5, 5]


def test_rsub_equal():
    c1 = [1, 2, 4]
    c2 = CustomList([3, 4, 5])
    res = c1 - c2

    assert isinstance(res, CustomList)
    assert res.lst == [-2, -2, -1]
    assert c1 == [1, 2, 4]
    assert c2.lst == [3, 4, 5]


def test_rsub_less():
    c1 = [1, 2]
    c2 = CustomList([3, 4, 5])
    res = c1 - c2

    assert isinstance(res, CustomList)
    assert res.lst == [-2, -2, -5]
    assert c1 == [1, 2]
    assert c2.lst == [3, 4, 5]


def test_rsub_greater():
    c1 = [1, 2, 5, 7]
    c2 = CustomList([3, 4, 5])
    res = c1 - c2

    assert isinstance(res, CustomList)
    assert res.lst == [-2, -2, 0, 7]
    assert c1 == [1, 2, 5, 7]
    assert c2.lst == [3, 4, 5]


def test_eq():
    c1 = CustomList([3, 4, 5])
    c2 = CustomList([4, 8])
    c3 = CustomList([1, 2, 3])

    assert c1 == c2
    assert not c1 == c3


def test_ne():
    c1 = CustomList([3, 4, 5])
    c2 = CustomList([4, 8])
    c3 = CustomList([1, 2, 3])

    assert c1 != c3
    assert not c1 != c2


def test_ge():
    c1 = CustomList([3, 4, 5])
    c2 = CustomList([4, 8])
    c3 = CustomList([1, 2, 13])

    assert c1 >= c2
    assert not c2 >= c3
    assert c3 >= c2


def test_gt():
    c1 = CustomList([3, 4, 5])
    c2 = CustomList([4, 8])
    c3 = CustomList([1, 2, 13])

    assert not c1 > c2
    assert not c2 > c3
    assert c3 > c2


def test_le():
    c1 = CustomList([3, 4, 5])
    c2 = CustomList([4, 8])
    c3 = CustomList([1, 2, 13])

    assert c1 <= c2
    assert c2 <= c3
    assert not c3 <= c2


def test_lt():
    c1 = CustomList([3, 4, 5])
    c2 = CustomList([4, 8])
    c3 = CustomList([1, 2, 13])

    assert not c1 < c2
    assert c2 < c3
    assert not c3 < c2


def test_str():
    c1 = CustomList([3, 4, 5])
    c2 = CustomList()

    assert str(c1) == "3 4 5 \nsum = 12"
    assert str(c2) == "\nsum = 0"
