import pytest

from src.lru_cache import LRUCache


class TestInit:
    def test_init_normal(self, lru_3_entry):
        assert lru_3_entry.limit == 3
        assert lru_3_entry._dct == {}

    def test_init_default(self, lru_default):
        assert lru_default.limit == 42
        assert lru_default._dct == {}

    def test_wrong_limit_type(self):
        with pytest.raises(TypeError):
            LRUCache('3')

    def test_wrong_empty_limit(self):
        with pytest.raises(ValueError):
            LRUCache(0)

    def test_wrong_limit_value(self):
        with pytest.raises(ValueError):
            LRUCache(-100)

    def test_attrs_available(self, lru_default):
        with pytest.raises(AttributeError):
            lru_default.x = 2


class TestGet:
    def test_nonexistent_key_empty(self, lru_default):
        assert lru_default.get("some_key") is None
        assert lru_default["some_key"] is None

    def test_nonexistent_key(self, lru_default):
        lru_default.set("key1", "val_1")
        lru_default.set("key2", "val_2")

        assert lru_default.get("key3") is None
        assert lru_default["key3"] is None

    def test_key_cached(self, lru_default):
        lru_default.set("key1", "val_1")

        assert lru_default.get("key1") == "val_1"

    def test_key_cached_getitem(self, lru_default):
        lru_default.set("key1", "val_1")

        assert lru_default["key1"] == "val_1"

    def test_key_cached_multiple(self, lru_3_entry):
        lru_3_entry.set("key1", "val_1")
        lru_3_entry.set("key2", "val_2")
        lru_3_entry.set("key3", "val_3")

        assert lru_3_entry.get("key1") == "val_1"
        assert lru_3_entry.get("key2") == "val_2"
        assert lru_3_entry.get("key3") == "val_3"

        assert lru_3_entry["key1"] == "val_1"
        assert lru_3_entry["key2"] == "val_2"
        assert lru_3_entry["key3"] == "val_3"

    def test_key_position_after_get(self, lru_default):
        lru_default.set("key1", "val_1")
        lru_default.set("key2", "val_2")
        lru_default.set("key3", "val_3")

        assert lru_default.get("key2") == "val_2"
        assert tuple(lru_default._dct) == ("key1", "key3", "key2")
        assert lru_default._dct.popitem() == ("key2", "val_2")

    def test_key_updating(self, lru_3_entry):
        lru_3_entry.set(2, 1)
        lru_3_entry.set(1, 1)
        lru_3_entry.set(3, 1)
        lru_3_entry.set(2, 3)
        lru_3_entry.set(4, 1)

        assert lru_3_entry.get(1) is None
        assert lru_3_entry.get(2) == 3


class TestSet:
    def test_not_hashable_key(self, lru_default):
        with pytest.raises(TypeError):
            lru_default.set([1, 2], [1, 2])

    def test_normal_set(self, lru_default):
        lru_default.set("key1", "val_1")
        assert lru_default["key1"] == "val_1"
        assert lru_default._dct == {"key1": "val_1"}

    def test_normal_setitem_(self, lru_default):
        lru_default["key1"] = "val_1"
        assert lru_default["key1"] == "val_1"
        assert lru_default._dct == {"key1": "val_1"}

    def test_set_multiple(self, lru_default):
        lru_default.set("key1", "val_1")
        lru_default.set("key2", "val_2")
        lru_default.set("key3", "val_3")

        assert lru_default.get("key1") == "val_1"
        assert lru_default.get("key2") == "val_2"
        assert lru_default.get("key3") == "val_3"
        assert tuple(lru_default._dct) == ("key1", "key2", "key3")

    def test_extra_element_without_get(self, lru_3_entry):
        lru_3_entry.set("key1", "val_1")
        lru_3_entry.set("key2", "val_2")
        lru_3_entry.set("key3", "val_3")
        assert tuple(lru_3_entry._dct) == ("key1", "key2", "key3")

        lru_3_entry.set("key4", "val_4")

        assert tuple(lru_3_entry._dct) == ("key2", "key3", "key4")
        assert lru_3_entry._dct.popitem() == ("key4", "val_4")

    def test_extra_element_with_get(self, lru_3_entry):
        lru_3_entry.set("key1", "val_1")
        lru_3_entry.set("key2", "val_2")
        lru_3_entry.set("key3", "val_3")
        assert tuple(lru_3_entry._dct) == ("key1", "key2", "key3")

        assert lru_3_entry.get("key2") == "val_2"
        assert tuple(lru_3_entry._dct) == ("key1", "key3", "key2")

        lru_3_entry.set("key4", "val_4")

        assert tuple(lru_3_entry._dct) == ("key3", "key2", "key4")
        assert lru_3_entry._dct.popitem() == ("key4", "val_4")
