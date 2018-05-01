import math
import pygame


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


class Collider:

    def __init__(self, position, size, is_circle=False):
        self.position = position
        self.size = size
        self.is_circle = is_circle
        if is_circle:
            width, height = size
            self.radius = (width+height)/4
        else:
            self.radius = 0

    def display(self, screen):
        x, y = int(self.position[0]), int(self.position[1])
        if self.is_circle:
            pygame.draw.circle(screen, (0, 250, 0), (x, y), int(self.radius), 1)
        else:
            pygame.draw.rect(screen, (0, 250, 0), pygame.Rect(
                x, y, self.size[0], self.size[1]
            ), 1)

    def collides_with(self, collider):
        if self.is_circle and collider.is_circle:
            return self._check_circle_with_circle(self, collider)
        elif self.is_circle and not collider.is_circle:
            return self._check_circle_with_rectangle(self, collider)
        elif not self.is_circle and collider.is_circle:
            return self._check_circle_with_circle(collider, self)
        else:
            return self._check_rectangle_with_rectangle(self, collider)

    def _check_circle_with_circle(self, circle1, circle2):
        dist = distance(circle1.position, circle2.position)
        return dist <= circle1.radius + circle2.radius

    def _check_circle_with_rectangle(self, circle, collider):
        cx, cy = circle.position
        rx, ry = collider.position
        rwidth, rheight = collider.size

        # vertically
        if rx <= cx <= rx + rwidth:
            return ry - circle.radius <= cy <= ry + rheight + circle.radius

        # horizontally
        if ry <= cy <= ry + rheight:
            return rx - circle.radius <= cx <= rx + rwidth + circle.radius

        # by corners
        corners = collider.get_corners()
        for corner in corners:
            if distance(corner, circle.position) <= circle.radius:
                return True

    def _check_rectangle_with_rectangle(self, rect1, rect2):
        corners1 = rect1.get_corners()
        corners2 = rect2.get_corners()
        for corner1 in corners1:
            if rect2.contains_corner(corner1):
                return True
        for corner2 in corners2:
            if rect1.contains_corner(corner2):
                return True
        return False

    def get_corners(self):
        if self.is_circle:
            print("NO CORNERS AVAILABLE FOR CIRCLE COLLIDERS!")
        else:
            x, y = self.position
            width, height = self.size
            return [(x, y), 
                    (x + width, y), 
                    (x, y + height), 
                    (x + width, y + height)]

    def contains_corner(self, corner):
        cx, cy = corner
        rx, ry = self.position
        rwidth, rheight = self.size
        return rx <= cx <= rx + rwidth and ry <= cy <= ry + rheight
