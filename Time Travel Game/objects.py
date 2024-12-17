import pygame
import variables as v

ground = pygame.Rect(0, 1000, 1920, 80)
player = pygame.Rect((v.SCREEN_WIDTH-v.PLAYER_WIDTH)//2, (v.SCREEN_HEIGHT-v.PLAYER_HEIGHT)//2, v.PLAYER_WIDTH, v.PLAYER_HEIGHT)

start_button = pygame.image.load("./assets/start_game.png")
start_button = pygame.transform.scale(start_button, (300, 75))
start_button_rect = pygame.Rect((v.SCREEN_WIDTH//2-150), (v.SCREEN_HEIGHT//2-37.5), 300, 75)

quit_button = pygame.image.load("./assets/quit.png")
quit_button = pygame.transform.scale(quit_button, (200, 50))
#quit_button_rect = quit_button.get_rect()
quit_button_rect = pygame.Rect((v.SCREEN_WIDTH//2-100), (v.SCREEN_HEIGHT//2+37.5), 200, 50)

key = pygame.image.load("./assets/key.png")
key = pygame.transform.scale(key, (28, 48))
key_rect = key.get_rect()