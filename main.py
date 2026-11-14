# Imports
import pygame
import random
from src.lamp import Lamp
from src.obstacles import Obstacle
from src.ui import UI
from src.obstacles import Spark
from src.lighting import LightingSystem
from src.background import ParallaxBackground
from src.save_manager import SaveManager
from src.particles import EmberParticle
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE, BG_COLOR, LAMP_X, LAMP_Y, STATE_PLAYING, STATE_GAME_OVER, MIN_LIGHT_RADIUS, SPARK_RESTORE, MAX_LIGHT_RADIUS, PIPE_WIDTH, PIPE_GAP, STATE_MENU, STATE_SHOP, FLAME_THEMES

# Inits
pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

lamp = Lamp(LAMP_X, LAMP_Y) 
obstacles = []

ui = UI()
game_state = STATE_MENU
score = 0
death_reason = ""
session_sparks = 0

spawn_timer = 0.0

particles = []
particle_timer = 0.0
shake_timer = 0.0

lighting = LightingSystem() 

sparks = []

bg = ParallaxBackground()

save_mgr = SaveManager()

def get_active_theme():
    selected_id = save_mgr.data.get("selected_flame", "amber")
  
    for item in FLAME_THEMES.values():
        if item["id"] == selected_id:
            return item

    return FLAME_THEMES["1"]

lamp.set_theme(get_active_theme()["path"])



running = True

# Game loop
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
           running = False

        if event.type == pygame.KEYDOWN:

            if game_state == STATE_MENU:
                
                if event.key == pygame.K_SPACE:
                    game_state = STATE_PLAYING
                    lamp.flap()
                
                elif event.key == pygame.K_s:
                    game_state = STATE_SHOP

            elif game_state == STATE_PLAYING:
                if event.key == pygame.K_SPACE:
                
                    if game_state == STATE_PLAYING:
                                    
                        lamp.flap()

            
            elif game_state == STATE_GAME_OVER:
                    if event.key == pygame.K_SPACE:
                        lamp = Lamp(LAMP_X, LAMP_Y)
                        lamp.set_theme(get_active_theme()["path"])
                        obstacles.clear()
                        spawn_timer = 0.0
                        score = 0
                        game_state = STATE_PLAYING
                        session_sparks = 0
                        sparks.clear()
                        particles.clear()
                        obstacles.clear()

                    if event.key == pygame.K_m:
                        lamp = Lamp(LAMP_X, LAMP_Y)
                        lamp.set_theme(get_active_theme()["path"])

                        obstacles.clear()
                        spawn_timer = 0.0
                        score = 0
                        game_state = STATE_MENU
                        session_sparks = 0
                        sparks.clear()
                        particles.clear()
                        obstacles.clear()

            elif game_state == STATE_SHOP:
                
                if event.key in (pygame.K_m, pygame.K_ESCAPE):
                    game_state = STATE_MENU

                selected_key = None

                if event.key in (pygame.K_1, pygame.K_KP1):
                    selected_key = "1"
                
                elif event.key in (pygame.K_2, pygame.K_KP2):
                    selected_key = "2"

                elif event.key in (pygame.K_3, pygame.K_KP3):
                    selected_key = "3"

                if selected_key and selected_key in FLAME_THEMES:
                    theme = FLAME_THEMES[selected_key]
                    theme_id = theme["id"]
                    unlocked = save_mgr.data.get("unlocked_flames", [])

                    if theme_id in unlocked:
                        save_mgr.select_flame(theme_id)

                    else:
                        save_mgr.unlock_flame(theme_id, theme["cost"])

                    lamp.set_theme(get_active_theme()["path"])


            

                


    bg.update(dt)                

    if game_state == STATE_PLAYING:
        lamp.update(dt)

        particle_timer += dt
        if particle_timer >= 0.04:
            flame_color = get_active_theme()["color"]
            particles.append(EmberParticle(lamp.rect.left + 6, lamp.rect.centery, flame_color))
            particle_timer = 0.0

        for p in particles:
            p.update(dt)

        particles = [p for p in particles if p.lifetime > 0]
        

        for spark in sparks:

            spark.update(dt)

            if not spark.collected and lamp.rect.colliderect(spark.rect):
                spark.collected = True
                lamp.light_radius = min(MAX_LIGHT_RADIUS, lamp.light_radius + SPARK_RESTORE)
                session_sparks += 1
        
        sparks = [s for s in sparks if not s.is_off_screen() and not s.collected]

        if lamp.light_radius <= MIN_LIGHT_RADIUS:
            death_reason = "Out of Oil & light!"
            game_state = STATE_GAME_OVER
            shake_timer = 0.25
            
            save_mgr.update_high_score(score)
            save_mgr.add_sparks(session_sparks)
            session_sparks = 0

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

                offest_top = (obs.top_rect.x - lamp.rect.x, obs.top_rect.y - lamp.rect.y)
                offest_bottom = (obs.bottom_rect.x - lamp.rect.x, obs.bottom_rect.y - lamp.rect.y)

                if lamp.mask.overlap(obs.mask_top, offest_top):
                    death_reason = "Shattered by Stone!"
                    game_state = STATE_GAME_OVER
                    shake_timer = 0.25

                    save_mgr.update_high_score(score)
                    save_mgr.add_sparks(session_sparks)
                    session_sparks = 0

                elif lamp.mask.overlap(obs.mask_bottom, offest_bottom):
                    death_reason = "Electrocuted by Iron!"
                    game_state = STATE_GAME_OVER
                    shake_timer = 0.25

                    save_mgr.update_high_score(score)
                    save_mgr.add_sparks(session_sparks)
                    session_sparks = 0
        
               
        

    

        if lamp.rect.bottom >= SCREEN_HEIGHT or lamp.rect.top <= 0:
            death_reason = "Fell into the Dark!"
            game_state = STATE_GAME_OVER
            shake_timer = 0.25

            save_mgr.update_high_score(score)
            save_mgr.add_sparks(session_sparks)
            session_sparks = 0

        obstacles = [obs for obs in obstacles if not obs.is_off_screen()]
 



    screen.fill(BG_COLOR)

    bg.draw(screen)

    if game_state == STATE_MENU:
        ui.draw_satrt_menu(screen, save_mgr.data.get("high_score", 0), save_mgr.data.get("total_sparks", 0))

    elif game_state == STATE_SHOP:
        ui.draw_shop(screen, save_mgr.data.get("total_sparks", 0), 
                     save_mgr.data.get("unlocked_flames", ["amner"]),
                     save_mgr.data.get("selected_flame", "amber"))
    
    elif game_state in (STATE_PLAYING, STATE_GAME_OVER):
        for obs in obstacles:
            obs.draw(screen)
        
        for spark in sparks:
            spark.draw(screen)

        for p in particles:
            p.draw(screen)
        
        lamp.draw(screen)
        
            
        
        lighting.draw_light_mask(screen, lamp.rect.center, lamp.light_radius, get_active_theme()["color"])
        
        ui.draw_score(screen, score)


    
    
    if game_state == STATE_GAME_OVER:
        ui.draw_game_over(screen, death_reason, score)

    
    offset_x, offset_y = 0, 0
    if shake_timer > 0:
        shake_timer -= dt
        offset_x = random.randint(-6, 6)
        offset_y = random.randint(-6, 6)

    window.fill((0, 0, 0))
    window.blit(screen, (offset_x, offset_y))
    pygame.display.flip()

pygame.quit()