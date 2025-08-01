import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Initialize delta time variable
    dt = 0
    
    # Create groups for managing game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Set both groups as containers for the Player class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    # Create asteroid field (after setting containers)
    asteroid_field = AsteroidField()

    # Create player in the center of the screen (after setting containers)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
        
        # Update all updatable objects
        updatable.update(dt)
        
        # Check for collisions between asteroids and player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return
        
        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
        
        # Fill screen with black
        screen.fill("black")
        
        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)
        
        # Refresh the screen
        pygame.display.flip()
        
        # Limit to 60 FPS and get delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
