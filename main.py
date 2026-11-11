# Imports
import pygame
import random
from src.lamp import Lamp
from src.obstacles import Obstacle
from src.ui import UI
from src.obstacles import Spark
from src.lighting import LightingSystem
from src.background import ParallaxBackground
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE, BG_COLOR, LAMP_X, LAMP_Y, STATE_PLAYING, STATE_GAME_OVER, MIN_LIGHT_RADIUS, SPARK_RESTORE, MAX_LIGHT_RADIUS, PIPE_WIDTH, PIPE_GAP

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

sparks = []

bg = ParallaxBackground()

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

                elif game_state == STATE_GAME_OVER:

                    lamp = Lamp(LAMP_X, LAMP_Y)
                    obstacles.clear()
                    spawn_timer = 0.0
                    score = 0
                    game_state = STATE_PLAYING

                    sparks.clear()
                    obstacles.clear()

    if game_state == STATE_PLAYING:
        lamp.update(dt)
        bg.update(dt)

        for spark in sparks:

            spark.update(dt)

            if not spark.collected and lamp.rect.colliderect(spark.rect):
                spark.collected = True
                lamp.light_radius = min(MAX_LIGHT_RADIUS, lamp.light_radius + SPARK_RESTORE)
        
        sparks = [s for s in sparks if not s.is_off_screen() and not s.collected]

        if lamp.light_radius <= MIN_LIGHT_RADIUS:
            death_reason = "Out of Oil & light!"
            game_state = STATE_GAME_OVER

        spawn_timer += dt
        if spawn_timer >= 1.6:
            new_obs = Obstacle(SCREEN_WIDTH + 20)
            obstacles.append(new_obs)
            gap_top = new_obs.top_rect.height
            safe_min_y = gap_top + 25
            safe_max_y = gap_top + PIPE_GAP - 25
            spark_x = SCREEN_WIDTH + 20 + 170
            spark_y = random.randint(safe_min_y, safe_max_y)
            sparks.append(Spark(spark_x, spark_y))
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
        

    

        if lamp.rect.bottom >= SCREEN_HEIGHT or lamp.rect.top <= 0:
            death_reason = "Fell into the Dark!"
            game_state = STATE_GAME_OVER

        obstacles = [obs for obs in obstacles if not obs.is_off_screen()]
 



    screen.fill(BG_COLOR)

    bg.draw(screen)

    for obs in obstacles:
        obs.draw(screen)

    for spark in sparks:
        spark.draw(screen)

    lamp.draw(screen)

    

    lighting.draw_light_mask(screen, lamp.rect.center, lamp.light_radius)

    ui.draw_score(screen, score)
    
    if game_state == STATE_GAME_OVER:
        ui.draw_game_over(screen, death_reason, score)

    
    pygame.display.flip()

pygame.quit()