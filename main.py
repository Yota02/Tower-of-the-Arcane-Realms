import pygame
from game import Game


pygame.init()
pygame.display.set_caption("Tower of the Arcane Realms")

ecran_taille = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(ecran_taille)
background = pygame.image.load('assets/background/48.jpg')


        
game = Game()
running = True

while running:
    screen.blit(game.player.image, game.player.rect)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
    
    pygame.display.update()