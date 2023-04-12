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

play_bouton = pygame.image.load('assets/utilitaire/play_button.png')
play_rect = play_bouton.get_rect()
play_rect.x = (game.largeur_ecran - play_rect.width) / 2
play_rect.y = (game.hauteur_ecran - play_rect.height) / 2

quit_bouton1 = pygame.image.load('assets/utilitaire/quit_button.png')
quit_buton = pygame.transform.scale(quit_bouton1, (50, 50))
quit_rect = play_bouton.get_rect()
quit_rect.x = game.largeur_ecran - quit_rect.width + 20
quit_rect.y = game.hauteur_ecran - quit_rect.height + 20

male = pygame.image.load('assets/personnage/male/male_nu.png')
male_rect = male.get_rect()
male_rect.x = (game.largeur_ecran - male_rect.width) / 2 
male_rect.y = (game.hauteur_ecran - male_rect.height) / 2

female = pygame.image.load('assets/personnage/female/female_nu.png')
female_rect = female.get_rect()
female_rect.x = (game.largeur_ecran - female_rect.width) / 4
female_rect.y = (game.hauteur_ecran - female_rect.height) / 2

while running:
    
    if game.background == 1 or 2:
        screen.blit(background, (0, 0))

    if game.is_playing and game.background == 3:
        game.update(screen)
    elif game.is_playing and game.background == 2:
        screen.blit(male, (male_rect.x, male_rect.y) )
        screen.blit(female, (female_rect.x, female_rect.y))
    else:
        screen.blit(titre, (titre_x, titre_y))
        screen.blit(play_bouton, (play_rect.x, play_rect.y))
        screen.blit(quit_buton, (quit_rect.x, quit_rect.y))

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
            if play_rect.collidepoint(event.pos) and game.background == 1:
                game.is_playing = True
                game.background += 1
            elif quit_rect.collidepoint(event.pos) and game.background == 1:
                running = False
                pygame.quit()
            elif female_rect.collidepoint(event.pos) and game.background == 2:
                game.sex = 2
                game.background += 1
            elif male_rect.collidepoint(event.pos) and game.background == 2:
                game.sex = 1
                game.background += 1
            

    pygame.display.update()