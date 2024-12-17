import pygame
import variables as v
import objects as obj


def menu_screen():
    while v.menu_running:
        v.screen.fill((255, 255, 255))

        pygame.draw.rect(v.screen, (255, 255, 255), obj.quit_button_rect)
        pygame.draw.rect(v.screen, (255, 255, 255), obj.start_button_rect)

        v.screen.blit(obj.start_button, ((v.SCREEN_WIDTH//2-150), (v.SCREEN_HEIGHT//2-37.5)))
        v.screen.blit(obj.quit_button, ((v.SCREEN_WIDTH//2-100), (v.SCREEN_HEIGHT//2+37.5)))
        
        mouse_pos = pygame.mouse.get_pos()
        if obj.quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if obj.start_button_rect.collidepoint(mouse_pos):
                            v.menu_running = False
                            v.what_screen = "Lvl1"


            if event.type == pygame.QUIT:
                pygame.quit()
        
        v.clock.tick(v.FPS)
        pygame.display.update()