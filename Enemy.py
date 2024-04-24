
class Enemy:
    x = 0
    y = 650
    aux = 0
    health = None
    image = None
    speed = None
    track_length = 0

    def __init__(self):
        pass

    def movement(self, screen, round):
        self.aux = self.aux + 1
        self.track_length = self.aux * self.speed
        if round % 2 == 1:
            
            if self.track_length <= 640:
                self.y = self.y - self.speed
            else:
                self.x = self.x + self.speed
            screen.blit(self.image, (self.x, self.y))
            
        else:

            if self.track_length <= 935:
                self.x = self.x + self.speed
            else:
                self.y = self.y - self.speed
            screen.blit(self.image, (self.x, self.y))
        

    def detect_projectile(self, x, y):
        if abs(self.x - x) < 40 and abs(self.y - y) < 40:
            return True
        
        elif abs(self.x - x) < 40 and abs(self.x - y) < 40:
            return True

    def pop(self):
        if self.health == 0:
            return True

    def end_of_track(self):
        if self.track_length >= 1450:
            return True
