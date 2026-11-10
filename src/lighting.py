import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class LightingSystem:

    def __init__(self):
        self.darkness = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_light_mask(self, target_surf, lamp_center, radius):
       
       dark_color = (25, 20, 45)
       light_color = (255, 245, 210)
       
       self.darkness.fill((25, 20, 45, 230))
       
       max_r = int(radius)
       if max_r > 0:
            for r in range(max_r, 0, -3):

                t = 1.0 - (r / max_r)
                factor = t ** 1.8 

                red = int(dark_color[0] + (light_color[0] - dark_color[0]) * factor)
                green = int(dark_color[1] + (light_color[1] - dark_color[1]) * factor)
                blue = int(dark_color[2] + (light_color[2] - dark_color[2]) * factor)

                pygame.draw.circle(self.darkness, (red, green, blue), lamp_center, r)
                
            target_surf.blit(self.darkness, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
