import pygame

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

    
    def mask(self):
        for i in self.obstacle_list:
            pygame.mask.from_surface(i)

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
        self.mask()
        self.random_obstacle()
        self.destroy()
        self.rect.x -= 10 