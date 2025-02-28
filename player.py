import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.shoot_timer = 0
        self.inertia = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0.4)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def move(self):
        self.inertia *= 0.97
        self.position += self.inertia
        if self.inertia.length() < 0.05:  # Adjust threshold as needed
            self.inertia = pygame.Vector2(0, 0)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]: 
            self.inertia += self.acceleration.rotate(self.rotation)
        if keys[pygame.K_s]:
            self.inertia -= self.acceleration.rotate(self.rotation)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.move()

        # wrap around the screen, keeping the player in frame
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
            


    def shoot(self):
        if 0 < self.shoot_timer:
            return

        shot = Shot(self.position.x, self.position.y) 
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED  
        self.inertia -= pygame.Vector2(0, 0.3).rotate(self.rotation) # firing recoil

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

