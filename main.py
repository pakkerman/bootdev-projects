import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
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

    

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteriod_field = AsteroidField()

    menu_title = pygame.font.Font("font/Pixeltype.ttf", 150).render("Asteroid", False, "White").convert()
    menu_title_rect = menu_title.get_rect(center = (x, y - 130))

    menu_message = pygame.font.Font("font/Pixeltype.ttf", 50).render("Press SPACE to start", False, "White").convert()
    menu_message_rect = menu_message.get_rect(center = (x, y + 120))

    game_active = False
    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if game_active:
                pass

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_active = True


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

            for item in drawable:
                item.draw(screen)

        else:
            screen.blit(menu_title, menu_title_rect)
            screen.blit(menu_message, menu_message_rect)


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()


