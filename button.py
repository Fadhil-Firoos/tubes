import pygame
from abc import ABC, abstractclassmethod
from config import *

# parrent class
class Button(ABC):
    def __init__(self):
        self.button_click = pygame.mixer.Sound('asset/audio/button.mp3')


    @abstractclassmethod
    def action(self):
        pass

# berfungsi untuk memulai permainan
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

# berfungsi untuk menampilkan menu setting / pause pada saat game dimulai
class Button_setting(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('asset/img/button/setting.png').convert_alpha()
        self.bg = pygame.image.load('asset/img/bg/board/end.png').convert_alpha()
        self.setting_message = font.render(f"Setting", False, ("#F0F0F0"))
        self.rect_board = self.bg.get_rect(center = (800, 350))
        self.setting_message_rect = self.setting_message.get_rect(center = (800, 200))
        self.x = 1500
        self.y = 80
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.cond = True
        self.jenis = "setting"
    
    def button_display(self):
        layar.blit(self.button, self.rect)

    def action(self, cond):
        return cond
    
    def display_board(self):
        layar.blit(self.bg, self.rect_board)
        layar.blit(self.setting_message, self.setting_message_rect)
        
    def update(self):
        self.action()

# berfungsi untuk menampilkan menu shop / pilih tema pada homepage
class Button_shop(Button,):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('asset/img/button/thema.png').convert_alpha()
        self.bg = pygame.image.load('asset/img/bg/board/shop.png').convert_alpha()
        self.close = pygame.image.load('asset/img/button/close.png').convert_alpha()
        self.thema1 = pygame.image.load('asset/img/thema/1.png').convert_alpha()
        self.thema1_pick = pygame.image.load('asset/img/thema/1_lock.png').convert_alpha()
        self.thema2 = pygame.image.load('asset/img/thema/2.png').convert_alpha()
        self.thema2_pick = pygame.image.load('asset/img/thema/2_lock.png').convert_alpha()
        self.shop_message = font.render(f"Shop", False, ("#F0F0F0"))
        self.rect_board = self.bg.get_rect(center = (800, 360))
        self.rect_close = self.bg.get_rect(center = (1650, 400))
        self.shop_rect = self.shop_message.get_rect(center = (800, 200))
        self.thema1_rect = self.thema1.get_rect(center = (600, 350))
        self.thema2_rect = self.thema2.get_rect(center = (1000, 350))
        self.x = 1500
        self.y = 80
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.cond = True
        self.jenis = "thema"
    
    def button_display(self):
        layar.blit(self.button, self.rect)    

    def display_board(self,thema):
        layar.blit(self.bg, self.rect_board)
        layar.blit(self.shop_message, self.shop_rect)
        layar.blit(self.close, self.rect_close)
        if thema == 1:
            layar.blit(self.thema1_pick, self.thema1_rect)
            layar.blit(self.thema2, self.thema2_rect)
        elif thema == 2:
            layar.blit(self.thema1, self.thema1_rect)
            layar.blit(self.thema2_pick, self.thema2_rect)
        


    def action(self, cond):
        return cond
        
    def update(self):
        self.action()

# berfungsi untuk melanjutkan permainan pada saat permainan di pause
class Button_resume(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('asset/img/button/resume.png').convert_alpha()
        self.x = 900
        self.y = 450
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.cond = True
        self.jenis = "resume"
    
    def button_display(self):
        layar.blit(self.button, self.rect)

    def action(self):
        return self.jenis
        
    def update(self):
        self.action()

# berfungsi untuk kembali ke homepage
class Button_home(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('asset/img/button/home.png').convert_alpha()
        self.button_game_over = pygame.image.load('asset/img/button/home.png').convert_alpha()
        self.x = 700
        self.y = 450
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.rect_game_over = self.button.get_rect(center = (800, 410))
        self.cond = True
        self.jenis = "home"
    
    def button_display(self):
        layar.blit(self.button, self.rect)
    
    def button_display_game_over(self):
        layar.blit(self.button_game_over, self.rect_game_over)

    def action(self):
        return self.jenis
        
    def update(self):
        self.action()

# jika tema yang terkunci belum dibuka class ini berfungsi untuk membeli tema yang belum terbuka
class Button_buy(Button):
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('asset/img/button/buy.png').convert_alpha()
        self.x = 1000
        self.y = 350
        self.rect = self.button.get_rect(center = (self.x, self.y))
        self.cond = True
        self.harga = 10
        self.jenis = "buy"
    
    def button_display(self):
        layar.blit(self.button, self.rect)

    def action(self, cond):
        return cond
        
    def update(self):
        self.action()