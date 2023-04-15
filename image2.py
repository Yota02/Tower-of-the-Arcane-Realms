import pygame
from game2 import Game2

pygame.init()
game = Game2()
selction_sex = False
selction_class = False

ecran_taille = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(ecran_taille)
background = pygame.image.load('assets/background/48.jpg')

titre = pygame.image.load('assets/utilitaire/texte/titre.png')
titre_rect = titre.get_rect(center=(game.largeur_ecran / 2, game.hauteur_ecran / 4))

sexe_text = pygame.image.load('assets/utilitaire/texte/sexe.png')
sexe_text_rect = sexe_text.get_rect(center=(game.largeur_ecran / 2, game.hauteur_ecran / 7))

class_text = pygame.image.load('assets/utilitaire/texte/classe.png')
class_text_rect = class_text.get_rect(center=(game.largeur_ecran / 2, game.hauteur_ecran / 7))

carac_text = pygame.image.load('assets/utilitaire/texte/carac.png')
carac_text_rect = carac_text.get_rect(center=(game.largeur_ecran / 2, game.hauteur_ecran / 7))

play_buton = pygame.image.load('assets/utilitaire/buton/play_button.png')
play_rect = play_buton.get_rect(center=(game.largeur_ecran / 2, game.hauteur_ecran / 2))
play_grossie = pygame.transform.scale(play_buton, (int(play_rect.width * 1.1), int(play_rect.height * 1.1)))
play_grossie_rect = play_grossie.get_rect(center=play_rect.center)

valider_buton = pygame.image.load('assets/utilitaire/buton/valider.png')
valider_buton_rect = valider_buton.get_rect(center=(game.largeur_ecran / 2, game.hauteur_ecran * 4 / 5))
valider_buton_grossie = pygame.transform.scale(valider_buton, (int(valider_buton_rect.width * 1.1), int(valider_buton_rect.height * 1.1)))
valider_buton_grossie_rect = valider_buton_grossie.get_rect(center=valider_buton_rect.center)

valider_buton_non = pygame.image.load('assets/utilitaire/buton/valider-non-selct.png')
valider_buton_non_rect = valider_buton_non.get_rect(center=(game.largeur_ecran / 2, game.hauteur_ecran * 4 / 5))
valider_buton_non_grossie = pygame.transform.scale(valider_buton_non, (int(valider_buton_non_rect.width * 1.1), int(valider_buton_non_rect.height * 1.1)))
valider_buton_non_grossie_rect = valider_buton_non_grossie.get_rect(center=valider_buton_non_rect.center)

quit_bouton1 = pygame.image.load('assets/utilitaire/buton/quit_button.png')
quit_buton = pygame.transform.scale(quit_bouton1, (50, 50))
quit_rect = quit_buton.get_rect()
quit_rect.x = game.largeur_ecran - quit_rect.width + 20
quit_rect.y = game.hauteur_ecran - quit_rect.height + 20

male = pygame.image.load('assets/personnage/male/male_nu.png')
male_rect = male.get_rect(center=(game.largeur_ecran / 4, game.hauteur_ecran / 2))
male_grossie = pygame.transform.scale(male, (int(male_rect.width * 1.1), int(male_rect.height * 1.1)))
male_grossie_rect = male_grossie.get_rect(center=male_rect.center)

female = pygame.image.load('assets/personnage/female/female_nu.png')
female_rect = female.get_rect(center=(game.largeur_ecran / 1.4, game.hauteur_ecran / 2))
female_grossie = pygame.transform.scale(female, (int(female_rect.width * 1.1), int(female_rect.height * 1.1)))
female_grossie_rect = female_grossie.get_rect(center=female_rect.center)

taille_image = (game.largeur_ecran // 6, game.hauteur_ecran // 3)

livre = pygame.image.load('assets/utilitaire/classe/livre.png')
livre = pygame.transform.scale(livre, taille_image)
livre_rect = livre.get_rect(center=(game.largeur_ecran // 5, game.hauteur_ecran // 2))
livre_grossie = pygame.transform.scale(livre, (int(livre_rect.width * 1.1), int(livre_rect.height * 1.1)))
livre_grossie_rect = livre_grossie.get_rect(center=livre_rect.center)

epee = pygame.image.load('assets/utilitaire/classe/epee.png')
epee = pygame.transform.scale(epee, taille_image)
epee_rect = epee.get_rect(center=(game.largeur_ecran * 2 // 5, game.hauteur_ecran // 2))
epee_grossie = pygame.transform.scale(epee, (int(epee_rect.width * 1.1), int(epee_rect.height * 1.1)))
epee_grossie_rect = epee_grossie.get_rect(center=epee_rect.center)

arc = pygame.image.load('assets/utilitaire/classe/arc.png')
arc = pygame.transform.scale(arc, taille_image)
arc_rect = arc.get_rect(center=(game.largeur_ecran * 3 // 5, game.hauteur_ecran // 2))
arc_grossie = pygame.transform.scale(arc, (int(arc_rect.width * 1.1), int(arc_rect.height * 1.1)))
arc_grossie_rect = arc_grossie.get_rect(center=arc_rect.center)

bouclier = pygame.image.load('assets/utilitaire/classe/bouclier.png')
bouclier = pygame.transform.scale(bouclier, taille_image)
bouclier_rect = bouclier.get_rect(center=(game.largeur_ecran * 4 // 5, game.hauteur_ecran // 2))
bouclier_grossie = pygame.transform.scale(bouclier, (int(bouclier_rect.width * 1.1), int(bouclier_rect.height * 1.1)))
bouclier_grossie_rect = bouclier_grossie.get_rect(center=bouclier_rect.center)

plus_buton = pygame.image.load('assets/utilitaire/buton/plus_button.png')
plus_rect = play_buton.get_rect(center=(game.largeur_ecran / 2, game.hauteur_ecran / 2))
plus_grossie = pygame.transform.scale(plus_buton, (int(plus_rect.width * 1.1), int(plus_rect.height * 1.1)))
plus_grossie_rect = plus_grossie.get_rect(center=plus_rect.center)