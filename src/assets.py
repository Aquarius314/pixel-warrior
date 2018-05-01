import pygame


class Assets:

    _assets = {}

    def __init__(self):
        self._assets['player_stand'] = pygame.image.load("assets/player/stand.png")
        self._assets['player_cast'] = pygame.image.load("assets/player/cast.png")
        self._assets['health'] = pygame.image.load("assets/heart.png")
        self._assets['mana'] = pygame.image.load("assets/mana.png")
        self._assets['exp'] = pygame.image.load("assets/exp.png")

    def get_asset(self, name):
        return self._assets[name]
