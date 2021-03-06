import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import time
# TODO: dodac autofire
# TODO: dodac pociski, któ®e zmieniajaą swoja wartość podczas przełączania na full scren

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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        alien_height = alien.rect.height - 59
        # print(alien_height)
        availible_space_y = self.settings.screen_height - (alien_height)//2
        # print(availible_space_y)
        number_aliens_y = availible_space_y // (2 * (alien_height))
        # print(number_aliens_y)
        for alien_number in range(number_aliens_y):
            alien = Alien(self)
            alien.y = alien_height + 2 * alien_height * alien_number
            alien.rect.y = alien.y
            self.aliens.add(alien)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
# wywalić pętle for z run_game!!! Run game ma byc czyste. Można zdefiniować nową metode np. self._update_bullets()
# i zdefnionować funkcję jako def _update_bullets(self), w którym damy poniższą petle. 
            for bullet in self.bullets.copy():
                if self.settings.Full_screen == 0:
                    if bullet.rect.right > 1200:
                        self.bullets.remove(bullet)
                elif self.settings.Full_screen == 1:
                    if bullet.rect.right > 2000:
                        self.bullets.remove(bullet)
            #print(len(self.bullets))
# zmienić obie wartości z hard coded, wtedy będzie można zrezygonwać z jednego ifa/elifa
            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

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
    #  new_bullet = Bullet(self)
    # self.bullets.add(new_bullet)
    # powyżej są nieograniczone poziski

        if len(self.bullets) < self.settings.bullets_allowed:
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
