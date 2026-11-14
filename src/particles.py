import pygame 
import random

class EmberParticle:
    def __init__(self, x, y, color):
        self.x = float(x)
        self.y = float(y)
        self.color = color

        self.vx = random.uniform(-140.0, -70.0)
        self.vy = random.uniform(-35.0, 35.0)

        self.lifetime = random.uniform(0.35, 0.65)
        self.max_lifetime = self.lifetime

        self.size = random.randint(3, 6)

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.lifetime -= dt

    def draw(self, surface):

        if self.lifetime > 0:
            ratio = self.lifetime / self.max_lifetime
            current_size = max(1, int(self.size * ratio))
            alpha = int(255 * ratio)

            part_surf = pygame.Surface((current_size * 2, current_size * 2), pygame.SRCALPHA)
            pygame.draw.circle(
                part_surf,(*self.color, alpha), (current_size, current_size), current_size
            )
            surface.blit(part_surf, (int(self.x - current_size), int(self.y - current_size)))