import pygame
from collider import Collider
from engine import Engine
from missile import Missile
import math
import time


class Player:

    MAX_HEALTH = 100
    MAX_MANA = 100

    missiles = []
    health = 0
    mana = 0
    experience = 0
    level = 0
    speed = 0
    jump_speed = 0
    name = "Nameless Warrior"
    vertical_speed = 0
    standing = True
    direction_left = True
    last_fire_time = time.time()
    fire_rate = 0.5

    color = (255, 0, 0)

    def __init__(self, x, y, parent):
        self.position = x, y
        self.size = 40, 60
        self.start_position = x, y
        self.previous_position = x, y
        self.reset_stats()
        self.collider = Collider(self.position, self.size)
        self.parent = parent

    def get_collider(self):
        self.collider.position = self.position
        return self.collider

    def reset_stats(self):
        self.position = self.start_position
        self.health = self.MAX_HEALTH
        self.mana = self.MAX_MANA
        self.speed = 4
        self.jump_speed = 10
        self.experience = 0
        self.level = 1
        self.fire_rate = 0.5
        self.vertical_speed = 0

    def display(self, screen, assets):
        x, y = self.position
        pic = assets.get_asset(self._choose_asset_name())
        screen.blit(pic, (int(x), int(y)))

        for missile in self.missiles:
            missile.display(screen, assets)

    def _choose_asset_name(self):
        if self.direction_left:
            return "player_left"
        else:
            return "player_right"

    def move_to(self, position):
        self.position = position

    def try_move(self, step):
        x, y = step
        px, py = self.position
        self.previous_position = self.position
        self.position = x + px, y + py
        collides = self.parent.engine.check_collisions(self, self.parent.colliding_rects)
        if collides:
            self.position = self.previous_position
            return self.try_smaller_step(x, y)
        return True

    def try_fire(self):
        if time.time() - self.last_fire_time > self.fire_rate:
            self.last_fire_time = time.time()
            self.fire()

    def fire(self):
        self.missiles.append(Missile(self.position, self.direction_left))

    def try_smaller_step(self, x, y):
        if math.fabs(x) > 1 or math.fabs(y) > 1:
            if x < 0:
                x += 1
            elif x > 0:
                x -= 1
            if y < 0:
                y += 1
            elif y > 0:
                y -= 1
            return self.try_move((x, y))
        return False

    def move_left(self):
        if self.try_move((-self.speed, 0)):
            self.color = (255, 0, 0)
            self.direction_left = True

    def move_right(self):
        if self.try_move((self.speed, 0)):
            self.color = (0, 255, 0)
            self.direction_left = False

    def move_up(self):
        if self.vertical_speed < 4:
            self.try_move((0, -self.jump_speed))

    def move_down(self):
        # self.try_move((0, self.speed))
        pass

    def get_position(self):
        return self.position

    def actions(self, game):
        self.gravity()
        for missile in self.missiles:
            missile.actions(game)

    def apply_gravity(self, gravity, max_gravity):
        self.vertical_speed = min(self.vertical_speed + gravity, max_gravity)

    def gravity(self):
        if self.vertical_speed > 0:
            falling = self.try_move((0, self.vertical_speed))
            if not falling:
                self.vertical_speed = 0
                self.standing = True
            else:
                self.standing = False
