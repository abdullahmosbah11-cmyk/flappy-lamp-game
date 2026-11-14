import pygame
import random
import math
from src.assets import load_sprite
from src.settings import PIPE_WIDTH, STONE_COLOR, IRON_COLOR, PIPE_GAP, SCROLL_SPEED, SCREEN_HEIGHT, ELECTRIC_COLOR, SPARK_COLOR, SPARK_SIZE, SPARK_RESTORE, SPARK_PATH, STONE_PATH, IRON_PATH

class Obstacle:
    def __init__(self, x, gap=PIPE_GAP, is_moving=False, move_speed=75.0):
        self.gap = gap
        self.min_y = 100
        self.max_y = SCREEN_HEIGHT - 100 - self.gap
        self.gap_y = float(random.randint(self.min_y, self.max_y))

        self.x = float(x)
        self.passed = False

        self.is_moving = is_moving
        self.vy = random.choice([-1, 1]) * move_speed if is_moving else 0.0
        
        self.img_top = load_sprite(STONE_PATH, size=(PIPE_WIDTH, SCREEN_HEIGHT))
        self.img_bottom = load_sprite(IRON_PATH, size=(PIPE_WIDTH, SCREEN_HEIGHT))

        self.top_rect = self.img_top.get_rect(bottomleft=(int(x), int(self.gap_y)))
        self.bottom_rect = self.img_bottom.get_rect(topleft=(int(x), int(self.gap_y + self.gap)))

        self.mask_top = pygame.mask.from_surface(self.img_top)
        self.mask_bottom = pygame.mask.from_surface(self.img_bottom)
    
    def update(self, dt, speed=SCROLL_SPEED):
        self.x -= speed * dt
        self.top_rect.x = int(self.x)
        self.bottom_rect.x = int(self.x)

        if self.is_moving:
            self.gap_y += self.vy * dt

            if self.gap_y <= self.min_y:
                self.gap_y = float(self.min_y)
                self.vy = abs(self.vy)

            elif self.gap_y >= self.max_y:
                self.gap_y = float(self.max_y)
                self.vy = -abs(self.vy)

            self.top_rect.bottom = int(self.gap_y)
            self.bottom_rect.top = int(self.gap_y + self.gap)
    
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
        

    def update(self, dt, speed=SCROLL_SPEED):
        self.x -= speed * dt 
        self.rect.x = int(self.x)

    def draw(self, screen):
        if not self.collected:
            glow_rect = self.glow.get_rect(center=self.rect.center)
            screen.blit(self.glow, glow_rect)
            screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.rect.right < 0
        
        

