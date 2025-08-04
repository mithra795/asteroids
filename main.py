# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    number = 1
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    ship = Player(x, y)
    while number > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        number += 1
        screen.fill("black")
        ship.draw(screen)
        pygame.display.flip()
        dt = (fps.tick(60) / 1000)
        ship.update(dt)
        number -= 1
        


if __name__ == "__main__":
    main()
