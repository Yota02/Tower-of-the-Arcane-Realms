import pygame
from player import Player
from monstre import Monstre

class Game2:

    def __init__(self):
        self.is_playing = True
        self.background = 4
        self.pressed = {}
        self.player = Player()
        self.all_player = pygame.sprite.Group()
        self.all_monstre = pygame.sprite.Group()
        self.hauteur_ecran = pygame.display.Info().current_h
        self.largeur_ecran = pygame.display.Info().current_w
        self.sex = 0
        self.classe = 0
        self.name = ''
        self.carac_point = 10

    def update(self, screen):

        if self.pressed.get(pygame.K_z) and self.player.rect.y < self.hauteur_ecran :
            self.player.mouvement_haut()
        elif self.pressed.get(pygame.K_s) and self.player.rect.y > self.hauteur_ecran:
            self.player.mouvement_bas()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > self.largeur_ecran:
            self.player.mouvement_gauche()
        elif self.pressed.get(pygame.K_d) and self.player.rect.x < self.largeur_ecran:
            self.player.mouvement_droite()
        elif self.pressed.get(pygame.K_m):
            pygame.quit()

        self.all_player.draw(screen)