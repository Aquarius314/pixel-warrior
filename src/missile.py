import pygame
import time
import random
from collider import Collider


class Missile:

    def __init__(self, position, left):
        self.active = True
        self.x, self.y = position
        self.left = left
        self.accuracy = 0
        self.speed = 10
        if left:
            self.speed *= -1

    def actions(self, game):
        if self.active:
            self.x += self.speed
            self.y += self.accuracy
            if game.engine.check_collisions(self, game.colliding_rects):
                self.active = False

    def get_collider(self):
        return Collider((self.x, self.y), (6, 6), is_circle=True)

    def display(self, screen, assets):
        if self.active:
            pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 6)

    def apply_gravity(self, gravity, max_gravity):
        return
