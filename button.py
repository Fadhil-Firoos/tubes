import pygame
from abc import ABC, abstractclassmethod
from config import *

class Button():
    def __init__(self):
        self.button_click = pygame.mixer.Sound('asset/audio/button.mp3')


    @abstractclassmethod
    def action(self):
        pass


class Button_play(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('asset/img/button/play.png').convert_alpha()
        self.x = 800
        self.y = 580
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.cond = True
    
    def button_display(self):
        layar.blit(self.button, self.rect)

    def action(self):
        pass

    def update(self):
        self.action()

class Button_setting(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('asset/img/button/setting.png').convert_alpha()
        self.bg = pygame.image.load('asset/img/bg/board/end.png').convert_alpha()
        self.rect_board = self.bg.get_rect(center = (800, 300))
        self.x = 1500
        self.y = 80
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.cond = True
        self.jenis = "setting"
    
    def button_display(self):
        layar.blit(self.button, self.rect)

    def action(self, cond):
        if cond:
            layar.blit(self.bg, self.rect_board)
        return cond
        
    def update(self):
        self.action()

class Button_shop(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('asset/img/button/thema.png').convert_alpha()
        self.x = 1500
        self.y = 80
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.cond = True
        self.jenis = "thema"
    
    def button_display(self):
        layar.blit(self.button, self.rect)

    def action(self):
        return self.jenis
        
    def update(self):
        self.action()