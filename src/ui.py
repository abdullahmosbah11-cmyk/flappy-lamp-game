import pygame 
from src.settings import SCREEN_HEIGHT, SCREEN_WIDTH, DANGER_COLOR, WHITE, GOLD_COLOR, FLAME_THEMES
class UI:
    def __init__(self):
        self.score_font = pygame.font.SysFont("consolas", 36, bold=True)
        self.text_font = pygame.font.SysFont("consolas", 22, bold=True)
        self.store_font = pygame.font.SysFont("consolas", 15, bold=True)

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

        menu_surf = self.text_font.render("Press M for Menu", True, (180, 180, 180))
        menu_rect = menu_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 65))
        screen.blit(menu_surf, menu_rect)

    def draw_satrt_menu(self, screen, high_score, total_sparks):
        title_surf = self.score_font.render("FLAPPY LAMP", True, GOLD_COLOR)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(title_surf, title_rect)
        
        hs_surf = self.text_font.render(f"HIGH SCORE: {high_score}", True, WHITE)
        hs_rect = hs_surf.get_rect(center=(SCREEN_WIDTH //2, SCREEN_HEIGHT // 2 - 30))
        screen.blit(hs_surf, hs_rect)
        
        sparks_surf = self.text_font.render(f"SPARKS: {total_sparks}", True, GOLD_COLOR)
        sparks_rect = sparks_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        screen.blit(sparks_surf, sparks_rect)
       
        play_surf = self.text_font.render("Press SPACE to Play", True, WHITE)
        play_rect = play_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70))
        screen.blit(play_surf, play_rect)
       
        shop_surf = self.text_font.render("Press S for Store", True, (100, 220, 255))
        shop_rect = shop_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))
        screen.blit(shop_surf, shop_rect)

    def draw_shop(self, screen, total_sparks, unlocked_flames, selected_flame):
        title_surf = self.score_font.render("FLAME STORE", True, GOLD_COLOR)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, 120))
        screen.blit(title_surf, title_rect)

        sparks_surf = self.text_font.render(f"YOUR SPARKS: {total_sparks}", True, WHITE)
        sparks_rect = sparks_surf.get_rect(center=(SCREEN_WIDTH // 2, 180))
        screen.blit(sparks_surf, sparks_rect)

        start_y = 260 

        for key, item in FLAME_THEMES.items():
            theme_id = item["id"]

            if theme_id == selected_flame:
                status_text= f"[{key}] {item['name']} (Equipped)"
                text_color = item["color"]

            elif theme_id in unlocked_flames:
                status_text = f"[{key}] {item['name']} [Press {key}]"
                text_color = WHITE

            else:
                status_text= f"[{key}] {item['name']} - {item['cost']} Sparks"
                text_color = (150, 150, 160)

            item_surf = self.store_font.render(status_text, True, text_color)
            item_rect = item_surf.get_rect(center=(SCREEN_WIDTH // 2, start_y))
            screen.blit(item_surf, item_rect)
            start_y += 55

        back_surf = self.text_font.render("Press M to Return to Menu", True, (255, 100, 100))
        back_rect = back_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80))
        screen.blit(back_surf, back_rect)

        

        