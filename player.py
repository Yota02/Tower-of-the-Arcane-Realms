import pygame
from projectil import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self) :
        super().__init__()
        self.vie = 100
        self.max_vie = 100
        self.attack = 1 
        self.vitesse = 5 
        self.image = pygame.image.load("assets/personnage/female/female_nu.png")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        

    def mouvement_haut(self):
        self.rect.y += self.vitesse

    def mouvement_bas(self):
        self.rect.y -= self.vitesse

    def mouvement_gauche(self):
        self.rect.x -= self.vitesse

    def mouvement_droite(self):
        self.rect.x += self.vitesse

    def fleche(self):
        fleche = Projectile.Fleche()
