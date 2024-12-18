import pygame
import variables as v
import objects as obj

def player_movement():
    
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

    if obj.player.colliderect(obj.key_rect):
        v.has_key = True

    v.clock.tick(v.FPS)
    pygame.display.update()