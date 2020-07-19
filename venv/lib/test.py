# próba zmniejszenia obrazka


def _create_fleet(self):



def _create_fleet(self):
    alien = Alien(self)
    alien_width = alien.rect.width
    availible_space_x = self.settings.screen_width - (2*alien_width)
    number_aliens_x = availible_space_x // (2*alien_width)
    for alien_number in range(number_aliens_x):
        alien = Alien(self)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)