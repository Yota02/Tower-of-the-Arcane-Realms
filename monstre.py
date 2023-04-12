import pygame 

class Monstre():

    def __init__(self, game, name):
        super().__init__(name)
        self.vie = 100
        self.max_vie = 100
        self.attack = 5 
        self.velocity = 5 
        self.porte = 1 
        self.magie = 0
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        
class squelette(Monstre):
    def __init__(self, game):
        super().__init__(game, "Squelette")
        self.vie = 100
        self.max_vie = 100
        self.attack
        self.velocity = 5
        self.porte = 6
        