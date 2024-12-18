import pygame
import variables as v
import objects as obj

def draw_text(text, font, text_col, x, y):
    text = font.render(text, True, text_col)
    v.screen.blit(text, (x, y))

def ui():
    v.screen.blit(obj.key, (50, 50))

    if v.has_key == True:
        num = 1
    elif v.has_key == False:
        num = 0
    else:
        num= 0

    draw_text(str(num), pygame.font.SysFont("Courier New", 50), (0, 0, 0), 90, 50)