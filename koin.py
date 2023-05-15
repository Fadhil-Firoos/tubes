import pygame
from config import *

class Koin(pygame.sprite.Sprite):
    def __init__(self, sum, cn):
        super().__init__()

        koin1 = pygame.image.load('asset/img/koin/1.png').convert_alpha()
        koin2 = pygame.image.load('asset/img/koin/2.png').convert_alpha()
        koin3 = pygame.image.load('asset/img/koin/3.png').convert_alpha()
        self.__koin_display = pygame.image.load('asset/img/koin/2.png').convert_alpha()
        self.__koin_list = [koin1,koin2,koin3]
        self.__koin_index = 0
        self.image = self.__koin_list[self.__koin_index]
        self.rect = self.image.get_rect(midbottom = (1660, 400))
        self.__koin_display_rect = self.image.get_rect(center = (50, 50))
        self.__total_koin = sum
        self.__koin = koin.render(f"{cn}", False, ("#404040"))
        self.__koin_in_run = koin.render(f"{sum}", False, ("#404040"))
        self.__koin_rect = self.__koin.get_rect(topleft = (80, 27))
        # data["coin"] += self.total_koin
        # foo(data["coin"])
        

    def mask(self):
        for i in self.__koin_list:
            pygame.mask.from_surface(i)

    def animation_state(self):
            self.__koin_index += 0.1
            if self.__koin_index >= len(self.__koin_list):
                self.__koin_index = 0
            self.image = self.__koin_list[int(self.__koin_index)]
    
    def display_koin(self):
        layar.blit(self.__koin_display, self.__koin_display_rect)
        layar.blit(self.__koin, self.__koin_rect)
    
    def display_koin_in_run(self):
        layar.blit(self.__koin_display, self.__koin_display_rect)
        layar.blit(self.__koin_in_run, self.__koin_rect)

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def koin_return(self, cn):
        return self.__total_koin + cn


    def update(self):
        self.mask()
        self.animation_state()
        self.rect.x -= 10 
