
class Tower:
    damage = None
    attack_speed = None
    image = None

    def __init__(self):
        pass

    def enemy_in_range(self):
        # return True
        pass

    def attack(self):
        if self.enemy_in_range():
            pass

    def draw(self, screen):
        screen.blit(self.image, (200, 230))
