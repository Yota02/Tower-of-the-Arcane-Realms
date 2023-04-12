import pygame
from player import Player


class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = {}
        
    def spawn_monster(self, monstre_class_nom):
        self.all_monstre.add(monstre_class_nom.__call__(self))