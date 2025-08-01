import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.turn_speed = PLAYER_TURN_SPEED
        self.shoot_timer = 0

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        # Decrease the shoot timer by dt
        self.shoot_timer -= dt
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= self.turn_speed * dt
        if keys[pygame.K_d]:
            self.rotation += self.turn_speed * dt
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        # Only shoot if the timer is 0 or less
        if self.shoot_timer <= 0:
            # Create a new shot at the player's position
            shot = Shot(self.position.x, self.position.y)
            
            # Set the shot's velocity in the direction the player is facing
            velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity *= PLAYER_SHOOT_SPEED
            shot.velocity = velocity
            
            # Set the timer to the cooldown value
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
