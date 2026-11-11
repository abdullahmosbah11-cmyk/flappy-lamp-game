import pygame 
from src.assets import load_sprite 
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG_LAYER1_PATH, BG_LAYER1_SPEED, BG_LAYER2_PATH, BG_LAYER2_SPEED

class ParallaxBackground:
    def __init__(self):
        self.img_layer1 = load_sprite(BG_LAYER1_PATH, size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.img_layer2 = load_sprite(BG_LAYER2_PATH, size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.layer1_x = 0.0 
        self.layer2_x = 0.0

    def update(self, dt):
        self.layer1_x = (self.layer1_x - BG_LAYER1_SPEED * dt) % SCREEN_WIDTH 
        self.layer2_x = (self.layer2_x - BG_LAYER2_SPEED * dt) % SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.img_layer1, (int(self.layer1_x), 0))
        screen.blit(self.img_layer1, (int(self.layer1_x) - SCREEN_WIDTH, 0))
        screen.blit(self.img_layer2, (int(self.layer2_x), 0))
        screen.blit(self.img_layer2, (int(self.layer2_x) - SCREEN_WIDTH, 0))