import pygame 
from src.assets import load_sprite_strip
from src.settings import    GRAVITY, FLAP_SPEED, MAX_FALL_SPEED, LAMP_COLOR, MAX_LIGHT_RADIUS, MIN_LIGHT_RADIUS, FUEL_DRAIN_RATE, LAMP_PATH, ROTATION_SPEED, MAX_DROP_ANGLE, FLAP_ANGLE

class Lamp:
    def __init__(self, x, y):
        self.frames = load_sprite_strip(LAMP_PATH, 32, 32)
        self.frame_index = 0.0

        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(int(x), int(y)))

        self.mask = pygame.mask.from_surface(self.image)

        self.x = float(x)
        self.y = float(y)
        self.vel_y = 0.0
        self.light_radius = float(MAX_LIGHT_RADIUS)

        self.angle = 0.0
    

    def flap(self):
        self.vel_y = FLAP_SPEED
        self.angle = FLAP_ANGLE

    def set_theme(self, sprite_path):
        self.frames = load_sprite_strip(sprite_path, 32, 32)
        base_image = self.frames[int(self.frame_index)]
        self.image = pygame.transform.rotate(base_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.vel_y = min(MAX_FALL_SPEED, self.vel_y + GRAVITY * dt)
        self.y += self.vel_y * dt
        self.rect.centery = int(self.y)
        self.light_radius = max(MIN_LIGHT_RADIUS, self.light_radius - FUEL_DRAIN_RATE * dt)

        self.frame_index += 8.0 * dt

        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]
        self.mask = pygame.mask.from_surface(self.image)

        if self.vel_y > 0:
            self.angle = max(MAX_DROP_ANGLE, self.angle - ROTATION_SPEED * dt)
        
        base_image = self.frames[int(self.frame_index)]
        self.image = pygame.transform.rotate(base_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        