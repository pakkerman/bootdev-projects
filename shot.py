import pygame
from constants import SHOT_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
        self.wrap_countdown = 2


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        if self.position.y <= 0 or SCREEN_HEIGHT <= self.position.y:
            self.wrap_countdown -= 1

        if self.wrap_countdown <= 0:
            self.kill()

        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT



