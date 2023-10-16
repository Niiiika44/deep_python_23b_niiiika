import pytest

from src.descriptors import MyDotaPersonality
from src.descriptors import MMR, FavoriteHero, FavoritePlayer


class TestProfile:
    def test_init(self):
        dota_profile = MyDotaPersonality("windranger",
                                         1337,
                                         "SR.Arteezy")
        assert dota_profile.fav_hero == "windranger"
        assert dota_profile.mmr == 1337
        assert dota_profile.fav_player == "SR.Arteezy"

    def test_class_attrs(self):
        with pytest.raises(AttributeError):
            MyDotaPersonality.fav_player
        with pytest.raises(AttributeError):
            MyDotaPersonality.fav_hero
        with pytest.raises(AttributeError):
            MyDotaPersonality.mmr


class TestHero:
    def test_init_correct(self):
        d1 = MyDotaPersonality("windranger",
                               1337,
                               "SR.Arteezy")
        d2 = MyDotaPersonality("LiCh",
                               1337,
                               "SR.Arteezy")
        assert d1.fav_hero == "windranger"
        assert d2.fav_hero == "LiCh"
    
    def test_change_init_correct(self):
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        assert d1.fav_hero == "ancient apparition"

        d1.fav_hero = "lion"
        assert d1.fav_hero == "lion"

    def test_not_str_init(self):
        with pytest.raises(TypeError):
            MyDotaPersonality(1,
                              1337,
                              "SR.Arteezy")
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        with pytest.raises(TypeError):
            d1.fav_hero = [1, 2, 4]

    def test_hero_not_favorite(self):
        with pytest.raises(ValueError):
            MyDotaPersonality("techies",
                              1337,
                              "SR.Arteezy")
        with pytest.raises(ValueError):
            MyDotaPersonality("123",
                              1337,
                              "SR.Arteezy")

    def test_set_name(self):
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        assert hasattr(d1, "fav_hero")
        assert hasattr(d1, "_fav_hero")
        assert d1._fav_hero == "ancient apparition"

    def test_setattr_with_err(self):
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        assert d1.fav_hero == "ancient apparition"

        with pytest.raises(TypeError):
            d1.fav_hero = 123

        assert d1.fav_hero == "ancient apparition"


class TestMMR:
    def test_init_correct(self):
        d1 = MyDotaPersonality("windranger",
                               0,
                               "SR.Arteezy")
        d2 = MyDotaPersonality("lich",
                               11999,
                               "SR.Arteezy")
        assert d1.mmr == 0
        assert d2.mmr == 11999

    def test_change_init_correct(self):
        d1 = MyDotaPersonality("ancient apparition",
                               1,
                               "SR.Arteezy")
        assert d1.mmr == 1

        d1.mmr = 26
        assert d1.mmr == 26

    def test_not_int_mmr(self):
        with pytest.raises(TypeError):
            MyDotaPersonality("ancient apparition",
                              "too many",
                              "SR.Arteezy")
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        with pytest.raises(TypeError):
            d1.mmr = [2, 2, 8]

    def test_negative_mmr(self):
        with pytest.raises(ValueError):
            MyDotaPersonality("ancient apparition",
                              -1000,
                              "SR.Arteezy")
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        with pytest.raises(ValueError):
            d1.mmr = -1

    def test_high_mmr(self):
        with pytest.raises(ValueError):
            MyDotaPersonality("ancient apparition",
                              12000,
                              "SR.Arteezy")
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        with pytest.raises(ValueError):
            d1.mmr = 13333

    def test_set_name(self):
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        assert hasattr(d1, "mmr")
        assert hasattr(d1, "_mmr")
        assert d1._mmr == 1337

    def test_setattr_with_err(self):
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        assert d1.mmr == 1337

        with pytest.raises(TypeError):
            d1.mmr = "123"

        assert d1.mmr == 1337


class TestPlayer:
    def test_init_correct(self):
        d1 = MyDotaPersonality("windranger",
                               0,
                               "SR.Arteezy")
        d2 = MyDotaPersonality("lich",
                               11999,
                               "TS.Mira")
        assert d1.fav_player == "SR.Arteezy"
        assert d2.fav_player == "TS.Mira"

    def test_change_init_correct(self):
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        assert d1.fav_player == "SR.Arteezy"

        d1.fav_player = "BetBoomTeam.GPK"
        assert d1.fav_player == "BetBoomTeam.GPK"

    def test_not_str_player(self):
        with pytest.raises(TypeError):
            MyDotaPersonality("ancient apparition",
                              1337,
                              ["r", "t", "z"])
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        with pytest.raises(TypeError):
            d1.fav_player = 123

    def test_wrong_player_name_format(self):
        with pytest.raises(ValueError):
            MyDotaPersonality("ancient apparition",
                              1337,
                              "Arteezy")
        with pytest.raises(ValueError):
            MyDotaPersonality("ancient apparition",
                              1337,
                              "SR:Arteezy")

        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        with pytest.raises(ValueError):
            d1.fav_player = "Miero"

    def test_set_name(self):
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        assert hasattr(d1, "fav_player")
        assert hasattr(d1, "_fav_player")
        assert d1._fav_player == "SR.Arteezy"

    def test_setattr_with_err(self):
        d1 = MyDotaPersonality("ancient apparition",
                               1337,
                               "SR.Arteezy")
        assert d1.fav_player == "SR.Arteezy"

        with pytest.raises(TypeError):
            d1.fav_player = 123

        assert d1.fav_player == "SR.Arteezy"
