import pygame


class Interface:

    def __init__(self, player):
        self.player = player

    def display(self, screen, assets):
        self._display_stats(screen, assets)
        # self._display_health(screen, assets)

    def _display_stats(self, screen, assets):
        # health
        pic = assets.get_asset("health")
        screen.blit(pic, (5, 5))
        healthbar = int((self.player.health/self.player.MAX_HEALTH)*100)
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(26, 5, 100, 16), 2)
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(26, 5, healthbar, 16))

        # mana
        pic = assets.get_asset("mana")
        screen.blit(pic, (5, 26))
        manabar = int((self.player.mana/self.player.MAX_MANA)*100)
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(26, 26, 100, 16), 2)
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(26, 26, manabar, 16))

        # experience
        pic = assets.get_asset("exp")
        screen.blit(pic, (5, 47))
        expbar = int((self.player.experience/self.player.MAX_EXP)*100)
        pygame.draw.rect(screen, (255, 160, 0), pygame.Rect(26, 47, 100, 16), 2)
        pygame.draw.rect(screen, (255, 160, 0), pygame.Rect(26, 47, expbar, 16))
