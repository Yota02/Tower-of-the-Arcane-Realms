import pygame 

class Projectile():

    def __init__(self, game, name):
        super().__init__(name)
        self.velocity = 5
        



class Fleche(Projectile):

    def __init__(self, game):
        super().__init__(game, "Squelette")

        