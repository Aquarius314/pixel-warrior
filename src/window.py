import pygame
from game import Game
import time


class Window:

    running = False
    last_frame = time.time()
    FPS = 60

    def __init__(self):
        self.game = Game()
        self.dimensions = 800, 600
        self.screen = pygame.display.set_mode(self.dimensions)
        pygame.init()

    def start(self):
        self.running = True
        while self.running:
            if self._execute_next_frame():
                self._handle_pygame_events()
                self._display()
                self._calculate()

    def _execute_next_frame(self):
        if time.time() - self.last_frame > (1/self.FPS):
            self.last_frame = time.time()
            return True
        else:
            return False

    def _handle_pygame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                info = "Window: KeyPressed: "
                if event.key == pygame.K_ESCAPE:
                    info += "ESCAPE"
                    self.running = False
                else:
                    self.game.handle_keydown(event.key)
                print(info)
            elif event.type == pygame.KEYUP:
                self.game.handle_keyup(event.key)

    def _display(self):
        self.screen.fill((0, 0, 0))    # BACKGROUND
        self.game.display_elements(self.screen)

        # must be at the end
        pygame.display.update()

    def _calculate(self):
        self.game.calculate()
