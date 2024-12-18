import pygame

# VARIABLES
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg_color = (196, 247, 101)

clock = pygame.time.Clock()
FPS = 60

gravity = 0
acceleration = 0

PLAYER_HEIGHT = 50
PLAYER_WIDTH = 100

what_screen = "Menu"

menu_running = True

platformed = True

has_key = False
key_x = 0
key_y = 0

door_x = 0
door_y = 0