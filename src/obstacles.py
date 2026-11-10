import pygame
import random
from src.settings import PIPE_WIDTH, STONE_COLOR, IRON_COLOR, PIPE_GAP, SCROLL_SPEED, SCREEN_HEIGHT, ELECTRIC_COLOR, SPARK_COLOR, SPARK_SIZE, SPARK_RESTORE

class Obstacle:
    def __init__(self, x):
        gap_y = random.randint(120, SCREEN_HEIGHT - 120 - PIPE_GAP)

        self.x = float(x)
        self.passed = False
        self.top_rect = pygame.Rect(x, 0, PIPE_WIDTH, gap_y)
        self.bottom_rect = pygame.Rect(x, gap_y + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - (gap_y + PIPE_GAP))
    
    def update(self, dt):
        self.x -= SCROLL_SPEED * dt
        self.top_rect.x = int(self.x)
        self.bottom_rect.x = int(self.x)
    
    def draw(self, screen):
        
        pygame.draw.rect(screen, STONE_COLOR, self.top_rect)
        pygame.draw.rect(screen, IRON_COLOR, self.bottom_rect)
        electric_hazard = pygame.Rect(self.bottom_rect.x, self.bottom_rect.y, self.bottom_rect.width, 6)
        pygame.draw.rect(screen, ELECTRIC_COLOR, electric_hazard)
    
    def is_off_screen(self):
        return self.top_rect.right < 0 
        
class Spark:
    def __init__(self, x, gap_y, pipe_gap):
        self.x = float(x)
        self.y = float(gap_y + pipe_gap // 2)
        self.rect = pygame.Rect(int(self.x), int(self.y), SPARK_SIZE, SPARK_SIZE)
        self.collected = False
    def update(self, dt):
        self.x -= SCROLL_SPEED * dt 
        self.rect.x = int(self.x)

    def draw(self, screen):
        if not self.collected:
            pygame.draw.circle(screen, SPARK_COLOR, self.rect.center, SPARK_SIZE // 2)

    def is_off_screen(self):
        return self.rect.right < 0
        
        

