import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        self.color = f"#cccccc"


    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        deg = random.uniform(20, 50)
        split_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, split_radius)

        asteroid_a.velocity = self.velocity.rotate(deg) * 1.2
        asteroid_b.velocity = self.velocity.rotate(-deg) * 1.2


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)








                
