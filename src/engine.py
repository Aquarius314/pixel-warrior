import pygame
import numpy as np


class Engine:

    gravity = 0.1
    MAX_GRAVITY = 13

    def check_collisions(self, body, colliders):
        for collider in colliders:
            for body_collider in body.get_colliders():
                if body_collider.collides_with(collider):
                    return True
        body.apply_gravity(self.gravity, self.MAX_GRAVITY)