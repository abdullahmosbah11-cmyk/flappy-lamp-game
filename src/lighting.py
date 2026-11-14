import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, MAX_LIGHT_RADIUS

class LightingSystem:

    def __init__(self):
        self.darkness = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw_light_mask(self, target_surf, lamp_center, radius, light_color=(255, 240, 190)):
              
       fuel_ratio = max(0.0, min(1.0, radius / MAX_LIGHT_RADIUS))
       
       dark_r = int(25 * fuel_ratio)
       dark_g = int(20 * fuel_ratio)
       dark_b = int(45 * fuel_ratio)
       dark_color = (dark_r, dark_g, dark_b)

       self.darkness.fill(dark_color)

       max_r = int(radius)
       if max_r > 0:
            for r in range(max_r, 0, -2):

                t = 1.0 - (r / max_r)
                factor = t ** 1.5 

                red = int(dark_color[0] + (light_color[0] - dark_color[0]) * factor)
                green = int(dark_color[1] + (light_color[1] - dark_color[1]) * factor)
                blue = int(dark_color[2] + (light_color[2] - dark_color[2]) * factor)

                pygame.draw.circle(self.darkness, (red, green, blue), lamp_center, r)
                
            target_surf.blit(self.darkness, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
