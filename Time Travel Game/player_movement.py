import pygame
import variables as v
import objects as obj

def player_movement():
    #Fills the screen to remove the player
    v.screen.fill((196, 247, 101))

    pygame.draw.rect(v.screen, (171,52,235), obj.player) #Draws the player
    pygame.draw.rect(v.screen, (0, 0, 0), obj.ground) #Draws the ground
    
    key = pygame.key.get_pressed()

    if key[pygame.K_w] and v.platformed:
        v.gravity = -12
        v.platformed = False
    if key[pygame.K_d]:
        v.acceleration = 6
    elif key[pygame.K_a]:
        v.acceleration = -6
    else:
        v.acceleration = 0
    
    obj.player.move_ip(v.acceleration, v.gravity)
    v.gravity += 1
    if obj.player.colliderect(obj.ground):
        v.platformed = True
        v.gravity = 0
        while obj.player.colliderect(obj.ground):
            obj.player.move_ip(0, -1)


    if obj.player.x > v.SCREEN_WIDTH - v.PLAYER_WIDTH:
        while obj.player.x > v.SCREEN_WIDTH - v.PLAYER_WIDTH:
            obj.player.move_ip(-1, 0)
    
    if obj.player.x < 0:
        while obj.player.x < 0:
            obj.player.move_ip(1, 0)

    v.clock.tick(v.FPS)
    pygame.display.update()