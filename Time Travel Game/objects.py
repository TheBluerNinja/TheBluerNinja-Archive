import pygame
import variables as v

v.key_x = v.SCREEN_WIDTH//2
v.key_y = 925

ground = pygame.Rect(0, 1000, 1920, 80)
player = pygame.Rect(150, 900, v.PLAYER_HEIGHT, v.PLAYER_WIDTH)

start_button = pygame.image.load("./assets/start_game.png")
start_button = pygame.transform.scale(start_button, (300, 75))
start_button_rect = pygame.Rect((v.SCREEN_WIDTH//2-150), (v.SCREEN_HEIGHT//2-37.5), 300, 75)

quit_button = pygame.image.load("./assets/quit.png")
quit_button = pygame.transform.scale(quit_button, (200, 50))
quit_button_rect = pygame.Rect((v.SCREEN_WIDTH//2-100), (v.SCREEN_HEIGHT//2+37.5), 200, 50)

key = pygame.image.load("./assets/key.png")
key = pygame.transform.scale(key, (28, 48))
key_rect = pygame.Rect(v.key_x, v.key_y, 28, 48)

door = pygame.image.load("./assets/door.png")
door = pygame.transform.scale(door, (32, 48))
door_rect = pygame.Rect(v.key_x, v.key_y, 32, 48)