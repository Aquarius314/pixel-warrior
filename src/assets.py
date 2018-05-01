import pygame


class Assets:

    _assets = {}
    custom_color = (100, 200, 100)
    modify_colors = True

    def __init__(self):
        self._assets['player_stand'] = pygame.image.load("assets/player/stand.png")
        self._assets['player_cast'] = pygame.image.load("assets/player/cast.png")

        if self.modify_colors:
            self._replace_assets_with_custom_color()

        self._assets['health'] = pygame.image.load("assets/heart.png")
        self._assets['mana'] = pygame.image.load("assets/mana.png")
        self._assets['exp'] = pygame.image.load("assets/exp.png")

    def _replace_assets_with_custom_color(self):
        for asset_name in self._assets.keys():
            new_pic = pygame.PixelArray(self._assets[asset_name])
            new_pic.replace((255, 0, 0), self.custom_color)
            self._assets[asset_name] = new_pic.surface

    def get_asset(self, name):
        return self._assets[name]
        # pic = self._assets[name]
        # if self.modify_colors:
        #     new_pic = pygame.PixelArray(pic)
        #     new_pic.replace((255, 0, 0), self.custom_color)
        #     return new_pic.surface
        # else:
        #     return pic
