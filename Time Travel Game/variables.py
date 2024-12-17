import pygame

# VARIABLES
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

gravity = 0
acceleration = 0

PLAYER_HEIGHT = 50
PLAYER_WIDTH = 50

what_screen = "Menu"

menu_running = True

platformed = True