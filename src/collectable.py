import pygame
import time
import math


class Collectable:

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def display(self, screen, assets):
        waving_y = int(10*(math.sin(time.time()*12/math.pi)) + self.y)
        pygame.draw.circle(screen, (200, 100, 250), (self.x, waving_y), self.radius, 4)
