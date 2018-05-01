import pygame
import time
import math
from collider import Collider


class Collectable:

    active = True
    colors = {
        0: (250, 250, 0),
        1: (250, 0, 0),
        2: (0, 0, 250)
    }

    def __init__(self, x, y, radius, type=0):
        self.x = x
        self.y = y
        self.waving_y = y
        self.radius = radius
        self.type = type
        if type not in self.colors.keys():
            print("INVALID TYPE OF COLLECTABLE!")

    def display(self, screen, assets):
        self.waving_y = int(10*(math.sin(time.time()*12/math.pi)) + self.y)
        pygame.draw.circle(screen, self.colors[self.type], (self.x, self.waving_y), self.radius, 6)

    def affect_player(self, player):
        if self.type == 0:
            player.add_money(1)
        elif self.type == 1:
            player.add_health(10)
        elif self.type == 2:
            player.add_mana(10)

        self.active = False

    def get_collider(self):
        return Collider((self.x, self.waving_y), (self.radius, self.radius), is_circle=True)
