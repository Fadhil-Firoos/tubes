import pygame

# class Get_coin(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         sum = 0
#         sum += 1
#         self.coin = sum
    
#     def koinn(self):
#         return self.coin
    
#     def update(self):
#         self.koinn()

class Koin(pygame.sprite.Sprite):
    def __init__(self, kondisi, sum):
        super().__init__()

        koin1 = pygame.image.load('asset/img/koin/1.png').convert_alpha()
        koin2 = pygame.image.load('asset/img/koin/2.png').convert_alpha()
        koin3 = pygame.image.load('asset/img/koin/3.png').convert_alpha()
        self.koin_list = [koin1,koin2,koin3]
        self.koin_index = 0
        
        self.image = self.koin_list[self.koin_index]
        self.rect = self.image.get_rect(midbottom = (1660, 400))
        self.total_koin = sum
        self.kond = kondisi

    def mask(self):
        for i in self.koin_list:
            pygame.mask.from_surface(i)

    def animation_state(self):
            self.koin_index += 0.1
            if self.koin_index >= len(self.koin_list):
                self.koin_index = 0
            self.image = self.koin_list[int(self.koin_index)]


    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


    def update(self):
        self.mask()
        self.animation_state()
        self.rect.x -= 10 
