import pygame 
from src.settings import SCREEN_HEIGHT, SCREEN_WIDTH, DANGER_COLOR, WHITE
class UI:
    def __init__(self):
        self.score_font = pygame.font.SysFont("consolas", 36, bold=True)
        self.text_font = pygame.font.SysFont("consolas", 22, bold=True)

    def draw_score(self, screen, score):
        
        score_surf = self.score_font.render(str(score), True, WHITE)
        score_rect = score_surf.get_rect(center=(SCREEN_WIDTH // 2, 45))
        screen.blit(score_surf, score_rect)

    def draw_game_over(self, screen, death_reason, score):

        reason_surf = self.text_font.render(death_reason, True, DANGER_COLOR)
        reason_rect = reason_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        screen.blit(reason_surf, reason_rect)

        retry_surf = self.text_font.render("Press SPACE to Retry", True, WHITE)
        retry_rect = retry_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25))
        screen.blit(retry_surf, retry_rect)

        