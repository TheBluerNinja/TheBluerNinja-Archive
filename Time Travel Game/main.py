import pygame
import variables as v
import player_movement as pm
import objects as obj
from Screens import menu as menu

pygame.init()

pygame.display.set_caption("Time Travel Game")

# GAME LOOP

running = True
while running:

    if v.what_screen == "Menu":
        menu.menu_screen()
    elif v.what_screen == "Lvl1":
        break

    pm.player_movement()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()