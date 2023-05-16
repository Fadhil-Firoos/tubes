import pygame
from abc import ABC, abstractclassmethod
from config import *

class Bg(ABC):
    def __init__(self):
        self.logo_surf = pygame.image.load('asset/img/bg/logo/Koceng_Loncat.png')
        self.logo_rect = self.logo_surf.get_rect(center = (800, 255))


    def display_logo(self):
        layar.blit(self.logo_surf,self.logo_rect)
    
    @abstractclassmethod
    def display_bg(self):
        pass

# untuk menampilkan tema 1
class Bg_1(Bg):
    def __init__(self):
        super().__init__()
        self.sky_surface = pygame.image.load('asset/img/bg/maps/sky1.png').convert_alpha()
        self.ground_surface = pygame.image.load('asset/img/bg/maps/ground1.png').convert_alpha()

    def display_bg(self):
        layar.blit(self.sky_surface, (0,0))
        layar.blit(self.ground_surface, (0,654))

# untuk menampilkan tema 2
class Bg_2(Bg):
    def __init__(self):
        super().__init__()
        self.sky_surface = pygame.image.load('asset/img/bg/maps/sky2.png').convert_alpha()
        self.ground_surface = pygame.image.load('asset/img/bg/maps/ground2.png').convert_alpha()

    def display_bg(self):
        layar.blit(self.sky_surface, (0,0))
        layar.blit(self.ground_surface, (0,654))