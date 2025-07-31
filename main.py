import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Initialize delta time variable
    dt = 0

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black
        screen.fill("black")
        
        # Refresh the screen
        pygame.display.flip()
        
        # Limit to 60 FPS and get delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
