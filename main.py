from msilib.schema import SelfReg
from typing import Self
import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk1 = pygame.image.load('asset/img/koceng/walk/1.png').convert_alpha()
        player_walk2 = pygame.image.load('asset/img/koceng/walk/2.png').convert_alpha()
        player_walk3 = pygame.image.load('asset/img/koceng/walk/3.png').convert_alpha()
        player_walk4 = pygame.image.load('asset/img/koceng/walk/4.png').convert_alpha()
        player_walk5 = pygame.image.load('asset/img/koceng/walk/5.png').convert_alpha()
        player_walk6 = pygame.image.load('asset/img/koceng/walk/6.png').convert_alpha()
        player_walk7 = pygame.image.load('asset/img/koceng/walk/7.png').convert_alpha()
        player_walk8 = pygame.image.load('asset/img/koceng/walk/8.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk2, player_walk3, player_walk4, player_walk5, player_walk6, player_walk7, player_walk8]

        player_jump1 = pygame.image.load('asset/img/koceng/jump/1.png').convert_alpha()
        player_jump2 = pygame.image.load('asset/img/koceng/jump/2.png').convert_alpha()
        player_jump3 = pygame.image.load('asset/img/koceng/jump/3.png').convert_alpha()
        player_jump4 = pygame.image.load('asset/img/koceng/jump/4.png').convert_alpha()
        player_jump5 = pygame.image.load('asset/img/koceng/jump/5.png').convert_alpha()
        player_jump6 = pygame.image.load('asset/img/koceng/jump/6.png').convert_alpha()
        player_jump7 = pygame.image.load('asset/img/koceng/jump/7.png').convert_alpha()
        player_jump8 = pygame.image.load('asset/img/koceng/jump/8.png').convert_alpha()
        player_jump9 = pygame.image.load('asset/img/koceng/jump/9.png').convert_alpha()
        player_jump10 = pygame.image.load('asset/img/koceng/jump/10.png').convert_alpha()
        self.player_jump = [player_jump1, player_jump2, player_jump3, player_jump4, player_jump5, player_jump6, player_jump7, player_jump8, player_jump9, player_jump10]
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (300, 680))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('asset/audio/jump.mp3')
        self.game_over_sound = pygame.mixer.Sound('asset/audio/game_over.mp3')

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 680:
            self.gravity = -24
            self.player_index = 0
            self.jump_sound.play()
            self.jump_sound.set_volume(0.15)

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 680:
            self.rect.bottom = 680
    
    def animation_state(self):
        if self.rect.bottom < 680:
            # jump
            self.player_index += 0.223
            if self.player_index >= len(self.player_jump):
                self.player_index = 0
            self.image = self.player_jump[int(self.player_index)]
        else:
            # walk
            self.player_index += 0.31
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def game_over_sound_play(self):
        self.game_over_sound.play()
        self.game_over_sound.set_volume(0.2)

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, index):
        super().__init__()
        obstacle_1 = pygame.image.load('asset/img/obstacle/1.png').convert_alpha()
        obstacle_2 = pygame.image.load('asset/img/obstacle/2.png').convert_alpha()
        obstacle_3 = pygame.image.load('asset/img/obstacle/3.png').convert_alpha()
        obstacle_4 = pygame.image.load('asset/img/obstacle/4.png').convert_alpha()
        obstacle_5 = pygame.image.load('asset/img/obstacle/5.png').convert_alpha()
        obstacle_6 = pygame.image.load('asset/img/obstacle/6.png').convert_alpha()
        obstacle_7 = pygame.image.load('asset/img/obstacle/7.png').convert_alpha()
        obstacle_8 = pygame.image.load('asset/img/obstacle/8.png').convert_alpha()
        obstacle_9 = pygame.image.load('asset/img/obstacle/9.png').convert_alpha()
        self.obstacle_list = [obstacle_1, obstacle_2, obstacle_3, obstacle_4, obstacle_5, obstacle_6, obstacle_7, obstacle_8, obstacle_9]

        self.obstacle_index = index
        self.image = self.obstacle_list[self.obstacle_index]
        self.rect = self.image.get_rect(bottomright = (1700, 680))
        self.obstacle_time = 0

    def random_obstacle(self):
        self.image = self.obstacle_list[self.obstacle_index]
    
    # def obstacle_timer(self):
    #     # timer
    #     self.obstacle_time = pygame.USEREVENT + 1
    #     pygame.time.set_timer(self.obstacle_time, 2000)
    #     self.random_obstacle()
    #     return self.obstacle_time

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.random_obstacle()
        self.rect.x -= 10 

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"score {current_time}", False, ("#F0F0F0"))
    score_rect = score_surf.get_rect(center = (800, 255))
    screen.blit(score_surf, score_rect)
    return current_time

# def obstacle_movement( obstacle_list):
#     if obstacle_list: 
#         for obtacle_rect in obstacle_list:
#             obtacle_rect.x -= 10

#             screen.blit(obstacle_surf,obtacle_rect)
#         return obstacle_list
#     else: return []

# def collision(kocengs, obstacles):
#     if obstacles:
#         for obstacle_rect in obstacles:
#             if kocengs.colliderect(obstacle_rect): 
#                 return False
#     return True
    
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        player.sprite.game_over_sound_play()
        obstacle_group.empty()
        bg_music.stop()
        return False
    else : 
        return True

# def koceng_animation():
#     # walking and jump animation fro kuceng
#     global koceng_surface, koceng_index
#     if koceng_rect.bottom < 680:
#         # jump
#         koceng_index += 0.223
#         if koceng_index >= len(koceng_jump):
#             koceng_index = 0
#         koceng_surface = koceng_jump[int(koceng_index)]
#     else:
#         # walk
#         koceng_index += 0.31
#         if koceng_index >= len(koceng_walk):
#             koceng_index = 0
#         koceng_surface = koceng_walk[int(koceng_index)]

pygame.init()
screen = pygame.display.set_mode((1600, 850))
pygame.display.set_caption("Koceng Loncat")
icon = pygame.image.load('asset/img/bg/icon/icon.png')
pygame.display.set_icon(icon)
game_active = False
start_time = 0
score = 0
status = 1
test_font = pygame.font.Font('asset/font/GAMERIA.ttf',75)
bg_music = pygame.mixer.Sound("asset/audio/backsound1.mp3")
bg_music.play()
bg_music.set_volume(0.1)
FPS = 60
clock = pygame.time.Clock()

# group
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


game_over = test_font.render("Game Over", False, ("#F0F0F0"))
game_over_rect = game_over.get_rect(center = (800, 200))


board_surf = pygame.image.load("asset/img/bg/board/end.png")
board_rect = board_surf.get_rect(center = (800, 255))

sky_surface = pygame.image.load('asset/img/bg/maps/1.png').convert()
ground_surface = pygame.image.load('asset/img/bg/maps/ground1.png').convert()
logo_surf = pygame.image.load('asset/img/bg/logo/Koceng_Loncat.png')

# obstacle_surf = pygame.image.load('asset/img/obstacle/1.png').convert_alpha()
# obstacle_rect = obstacle_surf.get_rect(bottomright = (1700, 680))
# obstacle_rect_list = []

# koceng_walk1 = pygame.image.load('asset/img/koceng/walk/1.png').convert_alpha()
# koceng_walk2 = pygame.image.load('asset/img/koceng/walk/2.png').convert_alpha()
# koceng_walk3 = pygame.image.load('asset/img/koceng/walk/3.png').convert_alpha()
# koceng_walk4 = pygame.image.load('asset/img/koceng/walk/4.png').convert_alpha()
# koceng_walk5 = pygame.image.load('asset/img/koceng/walk/5.png').convert_alpha()
# koceng_walk6 = pygame.image.load('asset/img/koceng/walk/6.png').convert_alpha()
# koceng_walk7 = pygame.image.load('asset/img/koceng/walk/7.png').convert_alpha()
# koceng_walk8 = pygame.image.load('asset/img/koceng/walk/8.png').convert_alpha()
# koceng_walk = [koceng_walk1, koceng_walk2, koceng_walk3, koceng_walk4, koceng_walk5, koceng_walk6, koceng_walk7, koceng_walk8]
# koceng_index = 0

# koceng_jump1 = pygame.image.load('asset/img/koceng/jump/1.png').convert_alpha()
# koceng_jump2 = pygame.image.load('asset/img/koceng/jump/2.png').convert_alpha()
# koceng_jump3 = pygame.image.load('asset/img/koceng/jump/3.png').convert_alpha()
# koceng_jump4 = pygame.image.load('asset/img/koceng/jump/4.png').convert_alpha()
# koceng_jump5 = pygame.image.load('asset/img/koceng/jump/5.png').convert_alpha()
# koceng_jump6 = pygame.image.load('asset/img/koceng/jump/6.png').convert_alpha()
# koceng_jump7 = pygame.image.load('asset/img/koceng/jump/7.png').convert_alpha()
# koceng_jump8 = pygame.image.load('asset/img/koceng/jump/8.png').convert_alpha()
# koceng_jump9 = pygame.image.load('asset/img/koceng/jump/9.png').convert_alpha()
# koceng_jump10 = pygame.image.load('asset/img/koceng/jump/10.png').convert_alpha()
# koceng_jump = [koceng_jump1, koceng_jump2, koceng_jump3, koceng_jump4, koceng_jump5, koceng_jump6, koceng_jump7, koceng_jump8, koceng_jump9, koceng_jump10]


# koceng_surface = koceng_walk[koceng_index]
# koceng_rect = koceng_surface.get_rect(midbottom = (200, 680))
# koceng_gravity = 0

koceng_stand = pygame.image.load('asset/img/intro/5.png').convert_alpha()
koceng_stand_rect = koceng_stand.get_rect(center = (800, 580))

logo_rect = logo_surf.get_rect(center = (800, 255))

# # timer
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
                # obstacle_rect_list.append(obstacle_surf.get_rect(bottomright = (randint(1700, 2000), 680)))

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if koceng_rect.collidepoint(event.pos) and koceng_rect.bottom >= 680 :
            #         koceng_gravity = -24

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE and koceng_rect.bottom >= 680:
            #         koceng_gravity = -24
            #         status = 1
            #         koceng_index = 0

        else : 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if status == 0:
                    bg_music.play()
                game_active = True
                # obstacle_rect.left = 1700
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

        # obstacle_rect.x -= 10   
        # if obstacle_rect.right <= 0 : 
        #     obstacle_rect.left = 1700
        # screen.blit(obstacle_surf,obstacle_rect)

        #player
        # koceng_gravity += 1
        # koceng_rect.y += koceng_gravity
        # if koceng_rect.bottom >= 680:
        #     koceng_rect.bottom = 680
        # koceng_animation()
        # screen.blit(koceng_surface, koceng_rect)
        player.draw(screen)
        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()
        # obstacle movment
        # obstacle_rect_list = obstacle_movement( obstacle_rect_list)

        # collision

        game_active = collision_sprite()
        # game_active = collision(koceng_rect, obstacle_rect_list)

        #game over
        if not game_active:
            # obstacle_rect_list.clear()
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
    clock.tick(FPS)