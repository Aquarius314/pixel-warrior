import numpy as np
import pygame
from collider import Collider


class MapPreparator:

    def get_optimised_rects(self, map):
        rects = []
        for x in range(len(map)):
            for y in range(len(map[0])):
                if map[x, y] == 255:
                    rect_x = x
                    rect_y = y
                    rect_width, rect_height = self.find_rect_size(map, x, y)
                    rect_fill_sum = np.sum(map[rect_x:rect_x+rect_width, rect_y:rect_y+rect_height])
                    if rect_fill_sum == rect_width*rect_height*255:
                        rects.append(Collider((rect_x, rect_y), (rect_width, rect_height)))
                        map[rect_x:rect_x + rect_width, rect_y:rect_y + rect_height] = 0
                    else:
                        rects.append(Collider((rect_x, rect_y), (1, 1)))
                        map[x, y] = 0
        return rects

    def find_rect_size(self, map, x, y):
        width = 0
        height = 0
        for i in range(x, len(map)):
            if map[i, y] == 255:
                width += 1
            else:
                break
        for i in range(y, len(map[0])):
            if map[x, i] == 255:
                height += 1
            else:
                break
        return width, height
