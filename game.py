import pygame
from player import Player



class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.all_player = pygame.sprite.Group()
        self.all_player.add(self.player)
        self.all_monstre = pygame.sprite.Group()
        self.pressed = {}
        self.hauteur_ecran = pygame.display.Info().current_h
        self.largeur_ecran = pygame.display.Info().current_w
        
        
    def spawn_monster(self, monstre_class_nom):
        self.all_monstre.add(monstre_class_nom.__call__(self))

    def update(self, screen):

        screen.blit(self.player.image, self.player.rect)

        if self.pressed.get(pygame.K_z) and self.player.rect.y < self.hauteur_ecran :
            self.player.mouvement_haut()
        elif self.pressed.get(pygame.K_s) and self.player.rect.y > self.hauteur_ecran:
            self.player.mouvement_bas()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > self.largeur_ecran:
            self.player.mouvement_gauche()
        elif self.pressed.get(pygame.K_d) and self.player.rect.x < self.largeur_ecran:
            self.mouvement_droite()
        elif self.pressed.get(pygame.K_m):
            pygame.quit()