from config import *

class Skor:
    def __init__(self,skor):
        self.current_skor = skor
        self.__score_surf = font.render(f"score {self.current_skor}", False, ("#F0F0F0"))
        self.__score_rect = self.__score_surf.get_rect(center = (800, 255))
    def display_score(self):
        layar.blit(self.__score_surf, self.__score_rect) 
        return self.current_skor
    

    def update(self):
        self.display_score()
