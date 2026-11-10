# Imports
import pygame
from src.lamp import Lamp
from src.obstacles import Obstacle
from src.ui import UI
from src.obstacles import Spark
from src.lighting import LightingSystem
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE, BG_COLOR, LAMP_X, LAMP_Y, STATE_PLAYING, STATE_GAME_OVER, MIN_LIGHT_RADIUS

# Inits
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

lamp = Lamp(LAMP_X, LAMP_Y) 
obstacles = []

ui = UI()
game_state = STATE_PLAYING
score = 0
death_reason = ""

spawn_timer = 0.0

lighting = LightingSystem() 

running = True

# Game loop
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
           running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if game_state == STATE_PLAYING:
                    
                    lamp.flap()
                    if lamp.light_radius <= MIN_LIGHT_RADIUS:
                        death_reason = "Out of Oil & light!"
                        game_state = STATE_GAME_OVER

                elif game_state == STATE_GAME_OVER:

                    lamp = Lamp(LAMP_X, LAMP_Y)
                    obstacles.clear()
                    spawn_timer = 0.0
                    score = 0
                    game_state = STATE_PLAYING

    if game_state == STATE_PLAYING:
        lamp.update(dt)

        spawn_timer += dt
        if spawn_timer >= 1.6:
            obstacles.append(Obstacle(SCREEN_WIDTH + 20))
            spawn_timer = 0.0

        for obs in obstacles:
        
                if not obs.passed and obs.top_rect.right < lamp.rect.left:
                    obs.passed = True 
                    score += 1
                obs.update(dt)
        
                if lamp.rect.colliderect(obs.top_rect):
                    death_reason = "Shattered by Stone!"
                    game_state = STATE_GAME_OVER
        
                if lamp.rect.colliderect(obs.bottom_rect):
                    death_reason = "Electrocuted by Iron!"
                    game_state = STATE_GAME_OVER
        

    

        if lamp.rect.bottom >= SCREEN_HEIGHT:
            death_reason = "Fell into the Dark!"
            game_state = STATE_GAME_OVER

            obstacles = [obs for obs in obstacles if not obs.is_off_screen()]
 



    screen.fill(BG_COLOR)

    for obs in obstacles:
        obs.draw(screen)

    lamp.draw(screen)

    lighting.draw_light_mask(screen, lamp.rect.center, lamp.light_radius)

    ui.draw_score(screen, score)
    
    if game_state == STATE_GAME_OVER:
        ui.draw_game_over(screen, death_reason, score)

    
    pygame.display.flip()

pygame.quit()