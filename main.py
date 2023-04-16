import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 850))
pygame.display.set_caption("Koceng Loncat")
clock = pygame.time.Clock()
game_active = False
status = 0
test_font = pygame.font.Font('asset/font/FunBlob.ttf',75)

game_over = test_font.render("Game Over", False, ("Black"))
game_over_rect = game_over.get_rect(center = (800, 255))
sky_surface = pygame.image.load('asset/bg/1.png').convert()
ground_surface = pygame.image.load('asset/bg/ground1.png').convert()
logo_surf = pygame.image.load('asset/bg/logo/Koceng Loncat.png')
logo_rect = logo_surf.get_rect(center = (800, 255))

obstacle_surf = pygame.image.load('asset/obstacle/1.png').convert_alpha()
obstacle_rect = obstacle_surf.get_rect(bottomright = (1700, 680))

koceng_surface = pygame.image.load('asset/koceng/run/5.png').convert_alpha()
koceng_rect = koceng_surface.get_rect(midbottom = (200, 680))
koceng_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if koceng_rect.collidepoint(event.pos) and koceng_rect.bottom >= 680 :
                    koceng_gravity = -24


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and koceng_rect.bottom >= 680:
                    koceng_gravity = -24
        else : 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                obstacle_rect.left = 1700
    
    if not game_active and status == 0:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,654))
        screen.blit(logo_surf, logo_rect)   
        
        koceng_gravity += 1
        koceng_rect.y += koceng_gravity
        if koceng_rect.bottom >= 680:
            koceng_rect.bottom = 680
        screen.blit(koceng_surface, koceng_rect)

    #draw all our elements
    #update everything
    
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,654))

        # pygame.draw.ellipse( screen, 'brown', pygame.Rect(200, 580, 100, 100))

        obstacle_rect.x -= 10   
        if obstacle_rect.right <= 0 : 
            obstacle_rect.left = 1700
        screen.blit(obstacle_surf,obstacle_rect)

        #player
        koceng_gravity += 1
        koceng_rect.y += koceng_gravity
        if koceng_rect.bottom >= 680:
            koceng_rect.bottom = 680
        screen.blit(koceng_surface, koceng_rect)

        #game over
        if obstacle_rect.colliderect(koceng_rect):
            game_active = False
            screen.blit(game_over, game_over_rect)  
            status = 1 



    pygame.display.update()
    clock.tick(60)