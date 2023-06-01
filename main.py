# import modul
import pygame
import time
import json
from sys import exit
from random import randint
from obstacle import *
from player import *
from skor import Skor
from config import *
from koin import *
from button import *
from bg import *
# deklarasi variable dengan value nama file json
filename = "data.json"


# method player bertabrakan dengan obstacle
def collision_sprite(a):
    # jika player bertabrakan akan dijalankan
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        player.sprite.game_over_sound_play() # play suara game_over_sound_play()
        obstacle_group.empty() # mengosongkan grup obstacle
        koin_group.empty()  #mengosongkan grup koin
        bg_music.stop() # backsound akan dimatikan
        return False, 0
    elif a == 3 : 
        return False, a
    else :
        return True, a
    
# method player mengenai koin
def coin():
    if pygame.sprite.spritecollide(player.sprite, koin_group, True):
        player.sprite.get_koin_sound_play() # play get_koin_sound_play()
        return True
    else:
        return False
    
# method unutk membaca data pada file json
def jsonread():
    with open(filename, "r") as f:
        temp = json.load(f)
        for data in temp:
            cn = data["coin"] 
            sk = data["skor"]
            by = data["buy"]
            thm = data["thema"]
        return cn, sk, by, thm
    
# method unutk mengedit data file json
def jsonedit(cn, sk, by, thm):
    temp1 = {}
    with open(filename, "r") as f:
        temp = json.load(f)
        del temp[0]
    with open(filename, "w") as f:
        json.dump(temp, f, indent = 4)
    with open(filename, "r") as f:
        temp = json.load(f)

    temp1["coin"]  = cn
    temp1["skor"] = sk
    temp1["buy"] = buy
    temp1["thema"] = thm
    temp.append(temp1)
    with open(filename, "w") as f:
        json.dump(temp, f, indent = 4)
    
    return cn, sk, by, thm


pygame.init()
cn, sk, by, thm = jsonread() # deklarasi variable cn, sk, by, thm = jsonread()
screen = layar # ukuran screen 
pygame.display.set_caption("Koceng Loncat") # menampilkan tulisan "Koceng Loncat"
icon = pygame.image.load('asset/img/bg/icon/icon.png') 
bg_music = pygame.mixer.Sound("asset/audio/backsound1.mp3") # backsound
pygame.display.set_icon(icon) # mengatur icon
game_active = False
coin_count= 0
status = 1
cond_button = ""
bg_music.set_volume(0.1) # set voulume
FPS = 60
clock = pygame.time.Clock()
skor_count = 0
cond = 0
cond_shop = 0
thema = thm
buy = by


# deklarasi objek
bg1 = Bg_1()
bg2 = Bg_2()

button_play = Button_play()        
button_shop = Button_shop()
button_setting = Button_setting()
button_resume = Button_resume()
button_home = Button_home()
button_buy = Button_buy()



obstacle_group = pygame.sprite.Group()
koin_group = pygame.sprite.Group()

player = pygame.sprite.GroupSingle()
player.add(Kucing_1())


# deklarasi vaiable unutuk game over
game_over = font.render("Game Over", False, ("#F0F0F0"))
game_over_rect = game_over.get_rect(center = (800, 150))
board_surf = pygame.image.load("asset/img/bg/board/end.png")
board_rect = board_surf.get_rect(center = (800, 255))

# timer unutuk berapa lama waktu jeda obtacle keluar setelah game dimulai
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)


while True:
    cn, sk, by, thm = jsonread() # deklarasi variable cn, sk, by, thm = jsonread()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(randint(0,8))) # random obtacle
                koin_group.add(Koin(coin_count, cn))

        elif game_active == False and status == 0: 
            button_home.button_display_game_over()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_home.rect_game_over.collidepoint(pygame.mouse.get_pos()):
                    game_active = False       
                    status = 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if status == 0:
                    bg_music.play()
                status = 2
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

                
                

    
# untuk tamppilan home 
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
 
        # unutk tampilan shop atau pilih tema
        if cond_shop == True:
            button_shop.display_board(thema)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_shop.rect_close.collidepoint(pygame.mouse.get_pos()):
                    cond_shop =  button_shop.action(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_shop.thema1_rect.collidepoint(pygame.mouse.get_pos()):
                    thema = 1
                    button_shop.display_board(thema)
                    jsonedit(cn, sk, buy, thema)
            if buy == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_shop.thema2_rect.collidepoint(pygame.mouse.get_pos()):
                        thema = 2
                        button_shop.display_board(thema)
                        jsonedit(cn, sk, buy, thema)
            else:
                button_buy.button_display()            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_buy.rect.collidepoint(pygame.mouse.get_pos()):
                        try :
                            print(cn)
                        except:
                            print("coin tidak terdefinisi")
                        else:
                            if cn < button_buy.harga:
                                buy = button_shop.action(False)
                            else:
                                buy = button_shop.action(True)
                                kn = cn - button_buy.harga
                            jsonedit(kn, sk, buy, thema)
                        finally:
                            print("succes")
            

        # untuk mengatur tampilan tema
        else:
            if thema == 1:
                bg1.display_bg()
                bg1.display_logo()
                Koin(coin_count, cn).display_koin()
            elif thema == 2:
                bg2.display_bg()
                bg1.display_logo()
                Koin(coin_count, cn).display_koin()
            button_shop.button_display()
            button_play.button_display()
            intro_message = font.render("Press Button to run", False, ("#f9981f"))
            intro_message_rect = intro_message.get_rect(center = (800, 450))
            screen.blit(intro_message, intro_message_rect)


    if skor_count > 0 and skor_count <= 0.01:
        bg_music.play()

    # untuk mengatur tampilan tema
    if game_active:
        if thema == 1:
            bg1.display_bg()
            Koin(coin_count, cn).display_koin_in_run()
        elif thema == 2:
            bg2.display_bg()
            Koin(coin_count, cn).display_koin_in_run()
        
        # mengatur skor
        score = Skor(int(skor_count))
        score.update()
        
        # menampilkan objek
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        koin_group.draw(screen)
        koin_group.update()
        button_play.update()

        # jika status 2 dan game_active True maka game dumulai
        if game_active == True and status == 2:
            skor_count += 0.01
            button_setting.button_display()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_setting.rect.collidepoint(pygame.mouse.get_pos()):
                        cond = button_setting.action(True)
            if cond == True:
                status = 3


        # memanggil method collision_sprite() mengatur jika player bertabrakan dengan obstacle
        game_active, status = collision_sprite(status)
        
        # jika get tru coin_count akan ditambahkan 1
        get = coin()
        if get == True:
            coin_count+= 1
            Koin(coin_count, cn)
        

        #jika status 0 dan game_active false maka game over
        if  game_active == False and status == 0:
            if skor_count > sk:
                score_message = font.render(f"Hight Score  {int(skor_count)}", False, ("#F0F0F0"))
            else:
                score_message = font.render(f"Your Score  {int(skor_count)}", False, ("#F0F0F0"))
            total_koin_message = font.render(f"Total Coin  {coin_count}", False, ("#F0F0F0"))

            score_message_rect = score_message.get_rect(center = (800, 250))
            total_koin_message_rect = score_message.get_rect(center = (800, 320))

            screen.blit(board_surf, board_rect)
            screen.blit(game_over, game_over_rect)

            screen.blit(score_message, score_message_rect)
            screen.blit(total_koin_message, total_koin_message_rect)

            intro_message = font.render("Press space to run", False, ("#f9981f"))
            intro_message_rect = intro_message.get_rect(center = (800, 570))
            screen.blit(intro_message, intro_message_rect)
            kn = Koin(coin_count, cn).koin_return(cn)
            if sk < int(skor_count):
                jsonedit(kn, int(skor_count), buy, thema)
            else:
                jsonedit(kn, sk, buy, thema)
            coin_count = 0
            skor_count = 0
    # jika sattus 3 dan game_active False maka game akan pause
    if game_active == False and status == 3:
        button_setting.display_board()
        button_resume.button_display()
        button_home.button_display()

        #melanjutkan game
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_resume.rect.collidepoint(pygame.mouse.get_pos()):
                cond = False
                game_active = True
                status = 2
        # kem bali ke home
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_home.rect.collidepoint(pygame.mouse.get_pos()):
                cond = False
                game_active = False            
                coin_count = 0
                skor_count = 0
                status = 1
                bg_music.stop()


    pygame.display.update()
    clock.tick(FPS)