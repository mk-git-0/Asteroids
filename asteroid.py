import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Immediately kill this asteroid
        self.kill()
        
        # If this is a small asteroid, we're done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        
        # Scale up the velocities by 1.2
        velocity1 *= 1.2
        velocity2 *= 1.2
        
        # Calculate new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids at the current position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2