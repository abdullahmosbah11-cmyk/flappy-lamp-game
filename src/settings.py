import pygame 

pygame.display.init()
screen_info = pygame.display.Info()

SCREEN_HEIGHT = int(screen_info.current_h * 0.8)
SCREEN_WIDTH = int(SCREEN_HEIGHT * (9 / 16))

FPS = 60 
TITLE = "flappy lamp"

BG_COLOR = (24, 28, 48)
LAMP_X = int(SCREEN_WIDTH * 0.25)
LAMP_Y = SCREEN_HEIGHT // 2
GRAVITY = 1400.0
FLAP_SPEED = -460.0
MAX_FALL_SPEED = 680.0
LAMP_COLOR = (255, 200, 65)

PIPE_WIDTH = 70
PIPE_GAP = 175
STONE_COLOR = (75, 70, 80)
IRON_COLOR = (45, 50, 62)
ELECTRIC_COLOR = (80, 220, 255)
SCROLL_SPEED = 210.0

STATE_PLAYING = 1
STATE_GAME_OVER = 2 
WHITE = (255, 255, 255)
DANGER_COLOR = (255, 80, 80)

MAX_LIGHT_RADIUS = 220.0
MIN_LIGHT_RADIUS = 40.0
FUEL_DRAIN_RATE = 12.0
DARKNESS_ALPHA = 240

SPARK_COLOR = (255, 230, 90)
SPARK_SIZE = 12 
SPARK_RESTORE = 50.0

BG_LAYER1_PATH = "assets/sprites/bg_layer1.png"
BG_LAYER2_PATH = "assets/sprites/bg_layer2.png"
BG_LAYER1_SPEED = 25.0 
BG_LAYER2_SPEED = 70.0

STONE_PATH = "assets/sprites/stone_top.png"
IRON_PATH = "assets/sprites/iron_bottom.png"
SPARK_PATH = "assets/sprites/spark.png"
LAMP_PATH = "assets/sprites/lamp.png"