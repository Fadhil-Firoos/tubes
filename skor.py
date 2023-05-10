import pygame
from config import *

class Skor:
    def __init__(self):
        self.start_time = 0
        self.current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
        self.score_surf = font.render(f"score {self.current_time}", False, ("#F0F0F0"))
        self.score_rect = self.score_surf.get_rect(center = (800, 255))

    def display_score(self):
        layar.blit(self.score_surf, self.score_rect)
        score = self.current_time
        return score
    

    def update(self):
        self.display_score()
