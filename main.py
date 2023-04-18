import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"score {current_time}", False, ("#F0F0F0"))
    score_rect = score_surf.get_rect(center = (800, 255))
    screen.blit(score_surf, score_rect)
    return current_time

pygame.init()
screen = pygame.display.set_mode((1600, 850))
pygame.display.set_caption("Koceng Loncat")
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0
status = 1
test_font = pygame.font.Font('asset/font/GAMERIA.ttf',75)


game_over = test_font.render("Game Over", False, ("#F0F0F0"))
game_over_rect = game_over.get_rect(center = (800, 200))


board_surf = pygame.image.load("asset/img/bg/board/end.png")
board_rect = board_surf.get_rect(center = (800, 255))

sky_surface = pygame.image.load('asset/img/bg/maps/1.png').convert()
ground_surface = pygame.image.load('asset/img/bg/maps/ground1.png').convert()
logo_surf = pygame.image.load('asset/img/bg/logo/Koceng_Loncat.png')

obstacle_surf = pygame.image.load('asset/img/obstacle/1.png').convert_alpha()
obstacle_rect = obstacle_surf.get_rect(bottomright = (1700, 680))

koceng_surface = pygame.image.load('asset/img/koceng/run/5.png').convert_alpha()
koceng_rect = koceng_surface.get_rect(midbottom = (200, 680))
koceng_gravity = 0

koceng_stand = pygame.image.load('asset/img/intro/5.png').convert_alpha()
koceng_stand_rect = koceng_stand.get_rect(center = (800, 580))

logo_rect = logo_surf.get_rect(center = (800, 255))

obstacle_timer = pygame.USEREVENT + 1

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
                    status = 1

        else : 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                obstacle_rect.left = 1700
                start_time = int(pygame.time.get_ticks() / 1000)
    

    if game_active == False and status == 1:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,654))
        screen.blit(logo_surf, logo_rect)   
        screen.blit(koceng_stand, koceng_stand_rect)
        intro_message = test_font.render("Press space to run", False, ("#f9981f"))
        intro_message_rect = intro_message.get_rect(center = (800, 400))
        screen.blit(intro_message, intro_message_rect)



    #draw all our elements
    #update everything
    
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,654))

        score = display_score()

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
            score_message = test_font.render(f"Your score  {score}", False, ("#F0F0F0"))
            score_message_rect = score_message.get_rect(center = (800, 300))
            screen.blit(board_surf, board_rect)
            screen.blit(game_over, game_over_rect)
            screen.blit(score_message, score_message_rect)
            intro_message = test_font.render("Press space to run", False, ("#f9981f"))
            intro_message_rect = intro_message.get_rect(center = (800, 580))
            screen.blit(intro_message, intro_message_rect)
            status = 0


    pygame.display.update()
    clock.tick(60)