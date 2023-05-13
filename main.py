import pygame
import time
from sys import exit
from random import randint
from obstacle import *
from player import *
from skor import Skor
from config import *
from koin import *
from button import *


    
def collision_sprite(a):
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        player.sprite.game_over_sound_play()
        obstacle_group.empty()
        koin_group.empty()  
        bg_music.stop()
        return False, 0
    elif a == 3 : 
        return False, a
    else :
        return True, a
    
def coin():
    if pygame.sprite.spritecollide(player.sprite, koin_group, True):
        player.sprite.get_koin_sound_play()
        return True
    else:
        return False
    
# def skor():
#     return current_skor

pygame.init()
screen = layar
pygame.display.set_caption("Koceng Loncat")
icon = pygame.image.load('asset/img/bg/icon/icon.png')
bg_music = pygame.mixer.Sound("asset/audio/backsound1.mp3")
pygame.display.set_icon(icon)
game_active = False
sum = 0
status = 1
cond_button = ""
bg_music.set_volume(0.1)
FPS = 60
clock = pygame.time.Clock()
skor_count = 0
cond = 0


# group
player = pygame.sprite.GroupSingle()
player.add(Kucing_1())

button_play = Button_play()        
button_shop = Button_shop()
button_setting = Button_setting()
button_resume = Button_resume()

obstacle_group = pygame.sprite.Group()
koin_group = pygame.sprite.Group()



game_over = font.render("Game Over", False, ("#F0F0F0"))
game_over_rect = game_over.get_rect(center = (800, 200))


board_surf = pygame.image.load("asset/img/bg/board/end.png")
board_rect = board_surf.get_rect(center = (800, 255))

sky_surface = pygame.image.load('asset/img/bg/maps/1.png').convert_alpha()
ground_surface = pygame.image.load('asset/img/bg/maps/ground1.png').convert_alpha()
logo_surf = pygame.image.load('asset/img/bg/logo/Koceng_Loncat.png')


# koceng_stand = pygame.image.load('asset/img/intro/5.png').convert_alpha()
# koceng_stand_rect = koceng_stand.get_rect(center = (800, 580))        


logo_rect = logo_surf.get_rect(center = (800, 255))

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(randint(0,8)))
                koin_group.add(Koin(False, sum))

        elif game_active == False and status == 0: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if status == 0:
                    bg_music.play()
                status = 2
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                

    

    if game_active == False and status == 1:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_play.rect.collidepoint(pygame.mouse.get_pos()):
                button_pressed = button_play.action()
                bg_music.play()
                status = 2
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_shop.rect.collidepoint(pygame.mouse.get_pos()):
                    cond = button_shop.action()
                    if cond == "thema":
                        print("thema")
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,654))
        screen.blit(logo_surf, logo_rect)
        button_shop.button_display()
        button_play.button_display()
        intro_message = font.render("Press Button to run", False, ("#f9981f"))
        intro_message_rect = intro_message.get_rect(center = (800, 450))
        screen.blit(intro_message, intro_message_rect)



    #draw all our elements
    #update everything
    
    if skor_count > 0 and skor_count <= 0.01:
        bg_music.play()

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,654))
        
        score = Skor(int(skor_count))
        score.update()
        
        player.draw(screen)
        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()

        koin_group.draw(screen)
        koin_group.update()

        button_play.update()

        if status == 2:
            skor_count += 0.01
            button_setting.button_display()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_setting.rect.collidepoint(pygame.mouse.get_pos()):
                        cond = button_setting.action(True)
            
        
            if cond == True:
                status = 3


        # collision

        game_active, status = collision_sprite(status)
        print(game_active, status)

        get = coin()
        if get == True:
            sum += 1
            Koin(get, sum)
        

        #game over
        if  game_active == False and status == 0:
            # obstacle_rect_list.clear()
            score_message = font.render(f"Your Score  {int(skor_count)}", False, ("#F0F0F0"))
            total_koin_message = font.render(f"Total Coin  {sum}", False, ("#F0F0F0"))
            print(score.current_skor)

            score_message_rect = score_message.get_rect(center = (800, 300))
            total_koin_message_rect = score_message.get_rect(center = (800, 370))

            screen.blit(board_surf, board_rect)
            screen.blit(game_over, game_over_rect)

            screen.blit(score_message, score_message_rect)
            screen.blit(total_koin_message, total_koin_message_rect)

            intro_message = font.render("Press space to run", False, ("#f9981f"))
            intro_message_rect = intro_message.get_rect(center = (800, 580))
            screen.blit(intro_message, intro_message_rect)
            sum  = 0
            skor_count = 0
            status = 0

    if game_active == False and status == 3:
        button_setting.display_board()
        button_resume.button_display()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_resume.rect.collidepoint(pygame.mouse.get_pos()):
                cond = False
                game_active = True
                status = 2


    pygame.display.update()
    clock.tick(FPS)