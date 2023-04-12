import pygame
from game import Game


pygame.init()
pygame.display.set_caption("Tower of the Arcane Realms")

hauteur_ecran = pygame.display.Info().current_h
largeur_ecran = pygame.display.Info().current_w
ecran_taille = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(ecran_taille)
background = pygame.image.load('assets/background/48.jpg')

game = Game()
running = True

while running:

    screen.blit(game.player.image, game.player.rect)
    screen.blit(background, (0, 0))

    pygame.display.flip()


    if game.pressed.get(pygame.K_z) and game.player.rect.y < hauteur_ecran :
        game.player.mouvement_haut()
    elif game.pressed.get(pygame.K_s) and game.player.rect.y > hauteur_ecran:
        game.player.mouvement_bas()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > largeur_ecran:
        game.player.mouvement_gauche()
    elif game.pressed.get(pygame.K_d) and game.player.rect.x < largeur_ecran:
        game.player.mouvement_droite()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type  == pygame.KEYUP:
            game.pressed[event.key] = False
    pygame.display.update()