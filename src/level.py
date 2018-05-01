import numpy
import pygame

# class containing specific level information
# (monsters, tower spots, walls, paths etc)


class Level:

    def __init__(self, level_number):
        level_file = "levels/" + str(level_number) + ".png"
        self.map = self._load_map(level_file)
        background_file = "levels/" + str(level_number) + "full.png"
        self.level_image = pygame.image.load(background_file)

    def get_map(self):
        return self.map

    def get_level_image(self):
        return self.level_image

    def _load_map(self, filename):
        return pygame.surfarray.pixels_red(pygame.image.load(filename))

    def _print_map_values(self):
        values = []
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                value = self.map[i, j]
                if not value in values:
                    values.append(value)
        print(values)