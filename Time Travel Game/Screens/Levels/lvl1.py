import pygame
import objects as obj
import variables as v
import ui

def lvl1():
    v.key_x = v.SCREEN_WIDTH//2
    v.key_y = 925
    
    v.door_x = v.SCREEN_WIDTH//2
    v.door_y = 925
    
    v.screen.fill(v.bg_color)

    ui.ui()
    
    if v.has_key == False:
        pygame.draw.rect(v.screen, v.bg_color, obj.key_rect)
        v.screen.blit(obj.key, ((v.key_x, v.key_y)))
    
    pygame.draw.rect(v.screen, (171,52,235), obj.player)
    
    pygame.draw.rect(v.screen, (31, 31, 31), obj.ground)