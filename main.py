import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from text import Text
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    Text.containers = (updatable, drawable)

    

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteriod_field = AsteroidField()
    text = Text()

    menu_title = pygame.font.Font("font/Pixeltype.ttf", 150).render("Asteroid", False, "White")
    menu_title_rect = menu_title.get_rect(center = (x, y - 130))

    menu_message = pygame.font.Font("font/Pixeltype.ttf", 50).render("Press SPACE to start", False, "White")
    menu_message_rect = menu_message.get_rect(center = (x, y + 120))


    game_active = False
    start_time = 0
    score = 0
    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if game_active:
                score = pygame.time.get_ticks() - start_time                

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_active = True
                        start_time = pygame.time.get_ticks()


        if game_active:
            updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.collision(player):
                    print("Game over!")
                    game_active = False

                for shot in shots:
                    if asteroid.collision(shot):
                        asteroid.split()
                        shot.kill()

            screen.fill("black")

            # score_text = pygame.font.Font("font/Pixeltype.ttf", 24).render(f"score: {score}", False, "White")
            # score_text_rect = score_text.get_rect(center = (SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40))
            # screen.blit(score_text, score_text_rect)


            for item in drawable:
                item.draw(screen)

        else:
            screen.blit(menu_title, menu_title_rect)
            screen.blit(menu_message, menu_message_rect)


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()


