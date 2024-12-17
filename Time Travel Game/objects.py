import pygame
import variables as v

ground = pygame.Rect(0, 640, 720, 80)
player = pygame.Rect((v.SCREEN_WIDTH-v.PLAYER_WIDTH)//2, (v.SCREEN_HEIGHT-v.PLAYER_HEIGHT)//2, v.PLAYER_WIDTH, v.PLAYER_HEIGHT)