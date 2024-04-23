
class Enemy:
    x = 0
    y = 500
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
        if self.track_length <= 500:
            self.y = self.y - self.speed
        else:
            self.x = self.x + self.speed
        
        screen.blit(self.image, (self.x, self.y))
        



    def detect_projectile(self, x, y):
        if abs(self.x - x) < 21 and abs(self.y - y) < 21:
            return True

    def pop(self):
        if self.health == 0:
            return True

    def end_of_track(self):
        if self.track_length >= 1300:
            return True
