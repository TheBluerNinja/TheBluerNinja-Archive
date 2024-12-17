import pygame
import variables as v

start_button = pygame.image.load("./assests/start_game.png")
start_button = pygame.transform.scale(start_button, (300, 75))
start_button_rect =  start_button.get_rect()

def menu_screen():
    while v.menu_running:
        v.screen.fill((255, 255, 255))

        v.screen.blit(start_button, ((v.SCREEN_WIDTH//2-150), (v.SCREEN_HEIGHT//2-37.5)))

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_pos):
                            v.menu_running = False
                            v.what_screen = "Lvl1"

            if event.type == pygame.QUIT:
                pygame.quit()
        
        v.clock.tick(v.FPS)
        pygame.display.update()