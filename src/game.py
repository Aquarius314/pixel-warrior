import pygame
from level import Level
from map_preparator import MapPreparator
from player import Player
from engine import Engine
from collider import Collider
from controller import Controller
from assets import Assets
from collectable import Collectable


class Game:

    colliding_rects = []
    collectables = [Collectable(320, 280, 10)]
    display_optimisation = False
    WALL_COLOR = (180, 220, 180)
    engine = Engine()
    controller = Controller()
    assets = Assets()

    def __init__(self):
        self.level = Level(1)
        self.map = self.prepare_map(self.level.get_map())
        self.level_image = self.level.get_level_image()
        self.player = Player(50, 0, self)

    def calculate(self):
        gravity_objects = [self.player]
        for gravity_obj in gravity_objects:
            self.engine.check_collisions(gravity_obj, self.colliding_rects)
        self.controller.apply_key_actions(self.player)
        self.player.actions(self)

    def prepare_map(self, map):
        self.colliding_rects += MapPreparator().get_optimised_rects(map)
        return map

    def display_elements(self, screen):
        self.display_map(screen)
        self.display_collectables(screen)
        self.player.display(screen, self.assets)

        if self.display_optimisation:
            self.display_colliding_rects(screen)

    def display_collectables(self, screen):
        for collectable in self.collectables:
            collectable.display(screen, self.assets)

    def display_map(self, screen):
        pic = self.level_image
        screen.blit(pic, pic.get_rect())

    def display_colliding_rects(self, screen):
        for rect in self.colliding_rects:
            rect.display(screen)
        for collider in self.player.get_colliders():
            collider.display(screen)
        # self.player.get_collider().display(screen)

    def handle_keydown(self, key):
        if key == pygame.K_o:
            self.display_optimisation = not self.display_optimisation
        else:
            self.controller.keyevent(key, pressed=True)

    def handle_keyup(self, key):
        self.controller.keyevent(key, pressed=False)


