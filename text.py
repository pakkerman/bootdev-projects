import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Text(pygame.sprite.Sprite):
    def __init__(self, size = 24):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.font = pygame.font.Font("font/Pixeltype.ttf", size)
        self.start_time = 0
        self.score = 0

    def draw(self, screen ):
        self.text = self.font.render(f"score: {self.score}", False, "white") 
        text_rect = self.text.get_rect(center = (SCREEN_WIDTH - 80, SCREEN_HEIGHT - 40))
        screen.blit(self.text, text_rect)

    def update(self, dt):
        self.score = pygame.time.get_ticks() - self.start_time



