import pygame


class Controller:

    def __init__(self):
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.space_pressed = False
        self.ctrl_pressed = False

    def keyevent(self, key, pressed=True):
        if key == pygame.K_LEFT:
            self.left_pressed = pressed
        elif key == pygame.K_RIGHT:
            self.right_pressed = pressed
        elif key == pygame.K_UP:
            self.up_pressed = pressed
        elif key == pygame.K_DOWN:
            self.down_pressed = pressed
        elif key == pygame.K_SPACE:
            self.space_pressed = pressed
        elif key == pygame.K_LCTRL:
            self.ctrl_pressed = pressed

    def apply_key_actions(self, player):
        if self.left_pressed:
            player.move_left()
        if self.right_pressed:
            player.move_right()
        if self.up_pressed:
            player.move_up()
        if self.down_pressed:
            player.move_down()

        if self.space_pressed:
            player.try_fire()
            player.is_casting = True
        else:
            player.is_casting = False

        if self.ctrl_pressed:
            player.reset_stats()
