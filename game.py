import pygame
from player import Player
from monstre import Monstre

class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player()
        self.all_player = pygame.sprite.Group()
        self.all_monstre = pygame.sprite.Group()
        self.pressed = {}
        self.hauteur_ecran = pygame.display.Info().current_h
        self.largeur_ecran = pygame.display.Info().current_w

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