import pytest

from src.descriptors import MyDotaPersonality
from src.descriptors import MMR, FavoriteHero, FavoritePlayer


@pytest.fixture()
def normal_init():
    dota_profile = MyDotaPersonality("windranger",
                                         1337,
                                         "SR.Arteezy")
    return dota_profile