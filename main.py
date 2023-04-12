import pygame
from game import Game

pygame.init()
pygame.display.set_caption("Tower of the Arcane Realms")

game = Game()
running = True

ecran_taille = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(ecran_taille)
background = pygame.image.load('assets/background/48.jpg')

titre = pygame.image.load('assets/utilitaire/titre.png')
titre_rect = titre.get_rect()
titre_x = (game.largeur_ecran - titre_rect.width) / 2
titre_y = (game.hauteur_ecran - titre_rect.height) / 4

start_bouton = pygame.image.load('assets/utilitaire/start_button.png')
start_rect = start_bouton.get_rect()
start_x = (game.largeur_ecran - start_rect.width) / 2
start_y = (game.hauteur_ecran - start_rect.height) / 2

while running:

    screen.blit(background, (0, 0))
    screen.blit(start_bouton, (start_x, start_y))
    
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(titre, (titre_x, titre_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type  == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                is_playing = True
