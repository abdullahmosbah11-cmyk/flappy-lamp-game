import pygame 
from src.settings import    GRAVITY, FLAP_SPEED, MAX_FALL_SPEED, LAMP_COLOR, MAX_LIGHT_RADIUS, MIN_LIGHT_RADIUS, FUEL_DRAIN_RATE

class Lamp:
    def __init__(self, x, y):
        self.image = pygame.Surface((36, 36))
        self.image.fill(LAMP_COLOR)
        self.x = float(x)
        self.y = float(y)
        self.vel_y = 0.0
        self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        self.light_radius = float(MAX_LIGHT_RADIUS)
    

    def flap(self):
        self.vel_y = FLAP_SPEED

    def update(self, dt):
        self.vel_y = min(MAX_FALL_SPEED, self.vel_y + GRAVITY * dt)
        self.y += self.vel_y * dt
        self.rect.centery = int(self.y)
        self.light_radius = max(MIN_LIGHT_RADIUS, self.light_radius - FUEL_DRAIN_RATE * dt)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        