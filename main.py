# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    number = 1
    while number > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        number += 1
        screen.fill("black")
        pygame.display.flip()
        number -= 1
        


if __name__ == "__main__":
    main()
