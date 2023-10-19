import pytest

from src.lru_cache import LRUCache


@pytest.fixture
def lru_default():
    return LRUCache()


@pytest.fixture
def lru_3_entry():
    return LRUCache(3)
