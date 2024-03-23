
class Enemy:
    x = -10
    y = 190
    aux = 0
    health = None
    image = None
    speed = None
    track_length = 0

    def __init__(self):
        pass

    def movement(self, screen):
        self.aux = self.aux + 1
        self.track_length = self.aux * self.speed
        if self.track_length <= 225:
            self.x = self.x + self.speed
        elif 225 < self.track_length <= 340:
            self.y = self.y - self.speed
        elif 340 < self.track_length <= 425:
            self.x = self.x - self.speed
        elif 425 < self.track_length <= 730:
            self.y = self.y + self.speed
        elif 730 < self.track_length <= 810:
            self.x = self.x - self.speed
        elif 810 < self.track_length <= 920:
            self.y = self.y - self.speed
        elif 920 < self.track_length <= 1145:
            self.x = self.x + self.speed
        elif 1145 < self.track_length <= 1280:
            self.y = self.y - self.speed
        elif 1280 < self.track_length <= 1355:
            self.x = self.x + self.speed
        elif 1355 < self.track_length <= 1540:
            self.y = self.y + self.speed
        elif 1540 < self.track_length <= 1680:
            self.x = self.x - self.speed
        elif 1540 < self.track_length <= 1690:
            self.x = self.x - self.speed
        elif 1690 < self.track_length <= 1815:
            self.y = self.y + self.speed

        screen.blit(self.image, (self.x, self.y))

    def detect_projectile(self, x, y):
        if abs(self.x - x) < 21 and abs(self.y - y) < 21:
            return True

    def pop(self):
        if self.health == 0:
            return True

    def end_of_track(self):
        if self.track_length >= 1820:
            return True
