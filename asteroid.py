import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_direction = random.uniform(20,50)
        new_vector1 = pygame.Vector2(self.velocity.x, self.velocity.y).rotate(split_direction)
        new_vector2 = pygame.Vector2(self.velocity.x, self.velocity.y).rotate(-split_direction)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_1.velocity = new_vector1 * 1.2
        split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_2.velocity = new_vector2 * 1.2
        

