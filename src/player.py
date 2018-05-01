import pygame
from collider import Collider
from engine import Engine
from missile import Missile
from interface import Interface
import math
import time


class Player:

    MAX_HEALTH = 100
    MAX_MANA = 100
    MAX_EXP = 100

    HEALTH_LOSS_RATE = 0.01
    MANA_GAIN_RATE = 0.04
    MANA_SPELL_COST = 10

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
    is_casting = False
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
        self.colliders = self._setup_colliders()
        self.parent = parent
        self.interface = Interface(self)

    def _setup_colliders(self):
        c1x, c1y = self.position
        c2x, c2y = self.position
        c1x += int(self.size[0]/2)
        c1y += int(self.size[1]/3)
        collider1 = Collider((c1x, c1y), (int(2*self.size[0]/3), int(2*self.size[1]/3)), is_circle=True)
        c2x += 10
        c2y += int(self.size[1]/3)
        collider2 = Collider((int(c1x-2-self.size[0]/3), c2y), (3*self.size[0]/4+3, int(2*self.size[1]/3)))

        return [collider1, collider2]

    def reset_stats(self):
        self.position = self.start_position
        self.health = self.MAX_HEALTH
        self.mana = self.MAX_MANA/2
        self.experience = 0
        self.speed = 4
        self.jump_speed = 10
        self.level = 1
        self.fire_rate = 0.5
        self.vertical_speed = 0

    def get_colliders(self):
        return self._setup_colliders()

    def display(self, screen, assets):
        x, y = self.position
        pic = self._prepare_asset(assets)
        screen.blit(pic, (int(x), int(y)))

        for missile in self.missiles:
            missile.display(screen, assets)

        self.interface.display(screen, assets)

    def _prepare_asset(self, assets):
        pic = assets.get_asset(self._choose_asset_name())
        if self.direction_left:
            pic = pygame.transform.flip(pic, True, False)
        return pic

    def _choose_asset_name(self):
        if self.is_casting:
            return "player_cast"
        return "player_stand"

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
        if self.mana >= self.MANA_SPELL_COST:
            if time.time() - self.last_fire_time > self.fire_rate:
                self.last_fire_time = time.time()
                self.fire()

    def fire(self):
        self.mana -= self.MANA_SPELL_COST
        midx = self.position[0] + int(self.size[0]/2)
        midy = self.position[1] + int(self.size[1]/2)
        self.missiles.append(Missile((midx, midy), self.direction_left))

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
        self._modify_stats()
        for missile in self.missiles:
            missile.actions(game)

    def _modify_stats(self):
        self.health -= self.HEALTH_LOSS_RATE
        self.mana = min(self.MAX_MANA, self.mana + self.MANA_GAIN_RATE)

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
