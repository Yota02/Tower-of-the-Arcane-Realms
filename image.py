import pygame
from game import Game

game = Game()

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
male_rect.x = (game.largeur_ecran - male_rect.width) / 4 
male_rect.y = (game.hauteur_ecran - male_rect.height) / 2

male_grossie = pygame.transform.scale(male, (int(male_rect.width * 1.1), int(male_rect.height * 1.1)))
male_grossie_rect = male_grossie.get_rect()
male_grossie_rect.x = (game.largeur_ecran + male_grossie_rect.width) / 4
male_grossie_rect.y = (game.hauteur_ecran - male_grossie_rect.height) / 2

female = pygame.image.load('assets/personnage/female/female_nu.png')
female_rect = female.get_rect()
female_rect.x = (game.largeur_ecran + female_rect.width) / 2
female_rect.y = (game.hauteur_ecran - female_rect.height) / 2

female_grossie = pygame.transform.scale(female, (int(female_rect.width * 1.1), int(female_rect.height * 1.1)))
female_grossie_rect = female_grossie.get_rect()
female_grossie_rect.x = (game.largeur_ecran + female_grossie_rect.width) / 2
female_grossie_rect.y = (game.hauteur_ecran - female_grossie_rect.height) / 2