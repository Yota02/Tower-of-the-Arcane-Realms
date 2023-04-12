import pygame 

class Monstre():

    def __init__(self, game, name):
        super().__init__(name)
        self.vie = 100



class squelette(Monstre):
    def __init__(self, game):
        super().__init__(game, "Squelette")
        