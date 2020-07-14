class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        #ciekawe czy uda się zdefiniowac taki event żeby obraz rosnął po naciśnięciu konkretnego klawisza?
        #chyba za duzo zmiennyych
        self.bg_color = (50, 50, 125)
        self.ship_speed = 2
        self.Full_screen = 0

        self.bullet_speed = 2.0
        self.bullet_width = 9
        self.bullet_height = 3
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3