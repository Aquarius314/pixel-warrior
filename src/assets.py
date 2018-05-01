import pygame


class Assets:

    _assets = {}

    def __init__(self):
        self._assets['player_left'] = pygame.image.load("assets/player/left.png")
        self._assets['player_right'] = pygame.image.load("assets/player/right.png")

    def get_asset(self, name):
        return self._assets[name]
