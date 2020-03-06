class Rain:
    def __init__(self, x, speed):
        self.x = x
        self.y = -50
        self.speed = speed

    def move(self):
        if self.y <= 620:
            pygame.draw.rect(root,(255, 0, 0), (self.x, self.y, 50, 50))
            self.y += 10
        else:
            self.y = 0-50