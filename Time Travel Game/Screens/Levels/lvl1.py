import pygame
import objects as obj
import variables as v


def lvl1():
    v.screen.fill((0, 0, 0))

    v.screen.blit(obj.key, ((v.SCREEN_WIDTH//2), (v.SCREEN_HEIGHT//2)))
    pygame.draw.rect(v.screen, (31, 31, 31), obj.ground)