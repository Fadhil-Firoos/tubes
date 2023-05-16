import pygame
from abc import ABC, abstractclassmethod

# Parrent class
class Player(pygame.sprite.Sprite, ABC):
    def __init__(self):
        super().__init__()

        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('asset/audio/jump.mp3')
        self.koin_get = pygame.mixer.Sound('asset/audio/get_coin.mp3')
        self.game_over_sound = pygame.mixer.Sound('asset/audio/game_over.mp3')

    @abstractclassmethod
    def masking(self):
        pass
            
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
    
    @abstractclassmethod
    def animation_state(self):
        pass

    def game_over_sound_play(self):
        self.game_over_sound.play()
        self.game_over_sound.set_volume(0.2)

    def get_koin_sound_play(self):
        self.koin_get.play()
        self.koin_get.set_volume(0.3)

    def update(self):
        self.masking()
        self.player_input()
        self.apply_gravity()
        self.animation_state()

# berfungsi unutk mengatur animasi player pada saat lompat atau berlari
class Kucing_1(Player):
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

    def masking(self):
        for masking1 in self.player_walk:
            pygame.mask.from_surface(masking1)
        for masking2 in self.player_jump:
            pygame.mask.from_surface(masking2)
        
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
