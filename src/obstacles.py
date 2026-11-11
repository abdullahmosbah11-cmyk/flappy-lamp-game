import pygame
import random
import math
from src.assets import load_sprite
from src.settings import PIPE_WIDTH, STONE_COLOR, IRON_COLOR, PIPE_GAP, SCROLL_SPEED, SCREEN_HEIGHT, ELECTRIC_COLOR, SPARK_COLOR, SPARK_SIZE, SPARK_RESTORE, SPARK_PATH, STONE_PATH, IRON_PATH

class Obstacle:
    def __init__(self, x):
        gap_y = random.randint(120, SCREEN_HEIGHT - 120 - PIPE_GAP)

        self.x = float(x)
        self.passed = False
        self.top_rect = pygame.Rect(x, 0, PIPE_WIDTH, gap_y)
        self.bottom_rect = pygame.Rect(x, gap_y + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - (gap_y + PIPE_GAP))
        self.img_top = load_sprite(STONE_PATH, size=(PIPE_WIDTH, gap_y))
        self.img_bottom = load_sprite(IRON_PATH, size=(PIPE_WIDTH, SCREEN_HEIGHT - (gap_y + PIPE_GAP)))

        self.mask_top = pygame.mask.from_surface(self.img_top)
        self.mask_bottom = pygame.mask.from_surface(self.img_bottom)
    
    def update(self, dt):
        self.x -= SCROLL_SPEED * dt
        self.top_rect.x = int(self.x)
        self.bottom_rect.x = int(self.x)
    
    def draw(self, screen):
        
        electric_hazard = pygame.Rect(self.bottom_rect.x, self.bottom_rect.y, self.bottom_rect.width, 6)
        screen.blit(self.img_top, self.top_rect)
        screen.blit(self.img_bottom, self.bottom_rect)
    
    def is_off_screen(self):
        return self.top_rect.right < 0 
        
class Spark:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.image = load_sprite(SPARK_PATH)
        self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        self.collected = False
        self.glow = pygame.Surface((SPARK_SIZE * 3, SPARK_SIZE * 3), pygame.SRCALPHA)
        pygame.draw.circle(self.glow, (255, 230, 90, 60), (SPARK_SIZE * 1.5, SPARK_SIZE * 1.5), SPARK_SIZE * 1.5)
        

    def update(self, dt):
        self.x -= SCROLL_SPEED * dt 
        self.rect.x = int(self.x)

    def draw(self, screen):
        if not self.collected:
            glow_rect = self.glow.get_rect(center=self.rect.center)
            screen.blit(self.glow, glow_rect)
            screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.rect.right < 0
        
        

