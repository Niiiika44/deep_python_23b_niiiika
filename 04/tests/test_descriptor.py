import pytest

from src.descriptors import MyDotaPersonality
from src.descriptors import MMR, FavoriteHero, FavoritePlayer


class TestProfile:
    def test_init(self, normal_init):
        assert normal_init.fav_hero == "windranger"
        assert normal_init.mmr == 1337
        assert normal_init.fav_player == "SR.Arteezy"

    def test_class_attrs(self):
        with pytest.raises(AttributeError):
            MyDotaPersonality.fav_player
        with pytest.raises(AttributeError):
            MyDotaPersonality.fav_hero
        with pytest.raises(AttributeError):
            MyDotaPersonality.mmr


class TestHero:
    def test_init_correct(self, normal_init):
        d2 = MyDotaPersonality("LiCh",
                               1337,
                               "SR.Arteezy")
        assert normal_init.fav_hero == "windranger"
        assert d2.fav_hero == "LiCh"
    
    def test_change_init_correct(self, normal_init):
        assert normal_init.fav_hero == "windranger"

        normal_init.fav_hero = "lion"
        assert normal_init.fav_hero == "lion"

    def test_not_str_init(self, normal_init):
        with pytest.raises(TypeError):
            MyDotaPersonality(1,
                              1337,
                              "SR.Arteezy")
        with pytest.raises(TypeError):
            normal_init.fav_hero = [1, 2, 4]

    def test_hero_not_favorite(self):
        with pytest.raises(ValueError):
            MyDotaPersonality("techies",
                              1337,
                              "SR.Arteezy")
        with pytest.raises(ValueError):
            MyDotaPersonality("123",
                              1337,
                              "SR.Arteezy")

    def test_set_name(self, normal_init):
        assert hasattr(normal_init, "fav_hero")
        assert hasattr(normal_init, "_fav_hero")
        assert normal_init._fav_hero == "windranger"

    def test_setattr_with_err(self, normal_init):
        assert normal_init.fav_hero == "windranger"

        with pytest.raises(TypeError):
            normal_init.fav_hero = 123

        assert normal_init.fav_hero == "windranger"


class TestMMR:
    def test_init_correct(self, normal_init):
        d1 = MyDotaPersonality("windranger",
                               0,
                               "SR.Arteezy")
        d2 = MyDotaPersonality("lich",
                               11999,
                               "SR.Arteezy")
        assert d1.mmr == 0
        assert d2.mmr == 11999
        assert normal_init.mmr == 1337

    def test_change_init_correct(self, normal_init):
        assert normal_init.mmr == 1337

        normal_init.mmr = 26
        assert normal_init.mmr == 26

    def test_not_int_mmr(self, normal_init):
        with pytest.raises(TypeError):
            MyDotaPersonality("ancient apparition",
                              "too many",
                              "SR.Arteezy")
        with pytest.raises(TypeError):
            normal_init.mmr = [2, 2, 8]

    def test_negative_mmr(self, normal_init):
        with pytest.raises(ValueError):
            MyDotaPersonality("ancient apparition",
                              -1000,
                              "SR.Arteezy")
        with pytest.raises(ValueError):
            normal_init.mmr = -1

    def test_high_mmr(self, normal_init):
        with pytest.raises(ValueError):
            MyDotaPersonality("ancient apparition",
                              12000,
                              "SR.Arteezy")
        with pytest.raises(ValueError):
            normal_init.mmr = 13333

    def test_set_name(self, normal_init):
        assert hasattr(normal_init, "mmr")
        assert hasattr(normal_init, "_mmr")
        assert normal_init._mmr == 1337

    def test_setattr_with_err(self, normal_init):
        assert normal_init.mmr == 1337

        with pytest.raises(TypeError):
            normal_init.mmr = "123"

        assert normal_init.mmr == 1337


class TestPlayer:
    def test_init_correct(self, normal_init):
        d1 = MyDotaPersonality("lich",
                               11999,
                               "TS.Mira")
        assert normal_init.fav_player == "SR.Arteezy"
        assert d1.fav_player == "TS.Mira"

    def test_change_init_correct(self, normal_init):
        assert normal_init.fav_player == "SR.Arteezy"

        normal_init.fav_player = "BetBoomTeam.GPK"
        assert normal_init.fav_player == "BetBoomTeam.GPK"

    def test_not_str_player(self, normal_init):
        with pytest.raises(TypeError):
            MyDotaPersonality("ancient apparition",
                              1337,
                              ["r", "t", "z"])
        with pytest.raises(TypeError):
            normal_init.fav_player = 123

    def test_wrong_player_name_format(self, normal_init):
        with pytest.raises(ValueError):
            MyDotaPersonality("ancient apparition",
                              1337,
                              "Arteezy")
        with pytest.raises(ValueError):
            MyDotaPersonality("ancient apparition",
                              1337,
                              "SR:Arteezy")
        with pytest.raises(ValueError):
            normal_init.fav_player = "Miero"

    def test_set_name(self, normal_init):
        assert hasattr(normal_init, "fav_player")
        assert hasattr(normal_init, "_fav_player")
        assert normal_init._fav_player == "SR.Arteezy"

    def test_setattr_with_err(self, normal_init):
        assert normal_init.fav_player == "SR.Arteezy"

        with pytest.raises(TypeError):
            normal_init.fav_player = 123

        assert normal_init.fav_player == "SR.Arteezy"
