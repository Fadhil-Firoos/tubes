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
from bg import *


    
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
coin_count= 0
status = 1
cond_button = ""
bg_music.set_volume(0.1)
FPS = 60
clock = pygame.time.Clock()
skor_count = 0
cond = 0
cond_shop = 0
thema = 1
buy = 0


# group
bg1 = Bg_1()
bg2 = Bg_2()

player = pygame.sprite.GroupSingle()
if thema == 1:
    player.add(Kucing_1())
elif thema == 2:
    player.add(Kucing_2())

button_play = Button_play()        
button_shop = Button_shop()
button_setting = Button_setting()
button_resume = Button_resume()
button_home = Button_home()
button_buy = Button_buy()

obstacle_group = pygame.sprite.Group()
koin_group = pygame.sprite.Group()



game_over = font.render("Game Over", False, ("#F0F0F0"))
game_over_rect = game_over.get_rect(center = (800, 200))



board_surf = pygame.image.load("asset/img/bg/board/end.png")
board_rect = board_surf.get_rect(center = (800, 255))

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)


while True:
    for event in pygame.event.get():
        get = coin()
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
            if cond_shop != True:
                if button_play.rect.collidepoint(pygame.mouse.get_pos()):
                    button_pressed = button_play.action()
                    bg_music.play()
                    status = 2
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_shop.rect.collidepoint(pygame.mouse.get_pos()):
                    cond_shop =  button_shop.action(True)
 

        if cond_shop == True:
            button_shop.display_board(thema)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_shop.rect_close.collidepoint(pygame.mouse.get_pos()):
                    cond_shop =  button_shop.action(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_shop.thema1_rect.collidepoint(pygame.mouse.get_pos()):
                    thema = 1
                    button_shop.display_board(thema)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_buy.rect.collidepoint(pygame.mouse.get_pos()):
                    if int(Koin(get, coin_count).total_koin) < button_buy.harga:
                        buy = button_shop.action(False)
                    else:
                        buy = button_shop.action(True)
                    print(buy)
            if buy == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_shop.thema2_rect.collidepoint(pygame.mouse.get_pos()):
                        thema = 2
                        button_shop.display_board(thema)
            else:
                button_buy.button_display()

        else:
            if thema == 1:
                bg1.display_bg()
                bg1.display_logo()
            elif thema == 2:
                bg2.display_bg()
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
        if thema == 1:
            bg1.display_bg()
        elif thema == 2:
            bg2.display_bg()
        
        score = Skor(int(skor_count))
        score.update()
        
        player.draw(screen)
        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()

        koin_group.draw(screen)
        koin_group.update()

        button_play.update()

        if game_active == True and status == 2:
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

        if get == True:
            coin_count+= 1
            Koin(get, coin_count)
        

        #game over
        if  game_active == False and status == 0:
            # obstacle_rect_list.clear()
            score_message = font.render(f"Your Score  {int(skor_count)}", False, ("#F0F0F0"))
            total_koin_message = font.render(f"Total Coin  {coin_count}", False, ("#F0F0F0"))

            score_message_rect = score_message.get_rect(center = (800, 300))
            total_koin_message_rect = score_message.get_rect(center = (800, 370))

            screen.blit(board_surf, board_rect)
            screen.blit(game_over, game_over_rect)

            screen.blit(score_message, score_message_rect)
            screen.blit(total_koin_message, total_koin_message_rect)

            intro_message = font.render("Press space to run", False, ("#f9981f"))
            intro_message_rect = intro_message.get_rect(center = (800, 580))
            screen.blit(intro_message, intro_message_rect)
            coin_count = 0
            skor_count = 0

    if game_active == False and status == 3:
        button_setting.display_board()
        button_resume.button_display()
        button_home.button_display()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_resume.rect.collidepoint(pygame.mouse.get_pos()):
                cond = False
                game_active = True
                status = 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_home.rect.collidepoint(pygame.mouse.get_pos()):
                cond = False
                game_active = False
                status = 1
                bg_music.stop()


    pygame.display.update()
    clock.tick(FPS)