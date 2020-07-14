import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class alieninvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        if self.settings.Full_screen == 0:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            pygame.display.set_caption('FISHDOM QUEST')
        elif self.settings.Full_screen != 0:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()



    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False




if __name__ == '__main__':
    ai = alieninvasion()
    ai.run_game()
