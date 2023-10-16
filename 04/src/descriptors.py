import re


class FavoriteHero:
    MY_FAV_HEROES = ["windranger",
                     "lich",
                     "ancient apparition",
                     "lion"]

    @classmethod
    def _validate_hero(cls, hero_name):
        if not isinstance(hero_name, str):
            raise TypeError("hero name should be a string")
        if not hero_name.lower() in cls.MY_FAV_HEROES:
            raise ValueError("no way")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self._validate_hero(value)
        setattr(instance, self.name, value)


class MMR:
    @staticmethod
    def _validate_mmr(mmr_num):
        if not isinstance(mmr_num, int):
            raise TypeError("mmr should be an integer")
        if mmr_num < 0:
            raise ValueError("mmr is non-negative")
        if mmr_num >= 12_000:
            raise ValueError("it can`t be real")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self._validate_mmr(value)
        setattr(instance, self.name, value)


class FavoritePlayer:
    PATTERN = r"\w+\.\w+"

    @classmethod
    def _validate_player(cls, player_name):
        if not isinstance(player_name, str):
            raise TypeError("player name should be a string")
        if not re.search(cls.PATTERN, player_name):
            raise ValueError("playername is TEAMNAME.NICKNAME")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self._validate_player(value)
        setattr(instance, self.name, value)


class MyDotaPersonality:
    fav_hero = FavoriteHero()
    mmr = MMR()
    fav_player = FavoritePlayer()

    def __init__(self, fav_hero, mmr, fav_player):
        self.fav_hero = fav_hero
        self.mmr = mmr
        self.fav_player = fav_player
