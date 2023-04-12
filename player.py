import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self) :
        super().__init__()
        self.vie = 100
        self.max_vie = 100
        self.attack = 1 
        self.vitesse = 5 
        self.image = pygame.image.load("assets/personnage/player.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300 