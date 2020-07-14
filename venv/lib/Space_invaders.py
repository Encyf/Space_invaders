import sys
import pygame
from settings import Settings
from ship import Ship


class alieninvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('FISHDOM QUEST')
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False


# TODO: Trzeba rozbić te check events na dwie funkcje - def KEYDOWN/KEYUP, ponieważ zaraz się zaplątam w tych
# wszystkich ifach


if __name__ == '__main__':
    ai = alieninvasion()
    ai.run_game()
