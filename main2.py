import pygame
from game2 import Game2
from image2 import *

pygame.init()
pygame.display.set_caption("Tower of the Arcane Realms")

font = pygame.font.SysFont("assets/utilitaire/8bitlimo.ttf", 32)
text_color = (0, 0, 0)
input_rect = pygame.Rect(50, 50, 200, 32)

game = Game2()
running = True
text = ""
active = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type  == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEMOTION:
            if valider_buton_rect.collidepoint(event.pos):
                valider_buton_affichee = valider_buton_grossie
                valider_buton_affichee_rect = valider_buton_grossie_rect
            else:
                valider_buton_affichee = valider_buton
                valider_buton_affichee_rect = valider_buton_rect
            if play_rect.collidepoint(event.pos) and game.background == 1:
                play_affichee = play_grossie
                play_affichee_rect = play_grossie_rect
            else:
                play_affichee = play_buton
                play_affichee_rect = play_rect
            if play_rect.collidepoint(event.pos) and game.background == 3:
                arc_affichee = arc_grossie
                arc_affichee_rect = arc_grossie_rect
            else:
                arc_affichee = arc
                arc_affichee_rect = arc_rect
            if female_rect.collidepoint(event.pos) and game.background == 2 and selction_sex == False:
                female_affichee = female_grossie
                female_affichee_rect = female_grossie_rect
            else:
                female_affichee = female
                female_affichee_rect = female_rect
            if male_rect.collidepoint(event.pos) and game.background == 2 and selction_sex == False:
                male_affichee = male_grossie
                male_affichee_rect = male_grossie_rect
            else:
                male_affichee = male
                male_affichee_rect = male_rect
            if livre_rect.collidepoint(event.pos) and game.background == 3:
                livre_affichee = livre_grossie
                livre_affichee_rect = livre_grossie_rect
            else:
                livre_affichee = livre
                livre_affichee_rect = livre_rect
            if bouclier_rect.collidepoint(event.pos) and game.background == 3:
                bouclier_affichee = bouclier_grossie
                bouclier_affichee_rect = bouclier_grossie_rect
            else:
                bouclier_affichee = bouclier
                bouclier_affichee_rect = bouclier_rect
            if epee_rect.collidepoint(event.pos) and game.background == 3:
                epee_affichee = epee_grossie
                epee_affichee_rect = epee_grossie_rect
            else:
                epee_affichee = epee
                epee_affichee_rect = epee_rect
            if arc_rect.collidepoint(event.pos) and game.background == 3:
                arc_affichee = arc_grossie
                arc_affichee_rect = arc_grossie_rect
            
            
            else:
                arc_affichee = arc
                arc_affichee_rect = arc_rect
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos) and game.background == 1:
                game.is_playing = True
                game.background += 1
            elif quit_rect.collidepoint(event.pos) and game.background == 1:
                running = False
                pygame.quit()
            elif valider_buton_rect.collidepoint(event.pos) and game.background == 2 and selction_sex:
                game.background += 1
            elif valider_buton_rect.collidepoint(event.pos) and game.background == 3 and selction_class :
                game.background += 1
            elif female_rect.collidepoint(event.pos) and game.background == 2:
                female_affichee = female_grossie
                female_affichee_rect = female_grossie_rect
                game.sex = 2
                selction_sex = True
            elif male_rect.collidepoint(event.pos) and game.background == 2:
                male_affichee = male_grossie
                male_affichee_rect = male_grossie_rect
                game.sex = 1
                selction_sex = True
            elif livre_rect.collidepoint(event.pos) and game.background == 3:
                livre_affichee  = livre_grossie
                livre_affichee_rect = livre_grossie_rect
                game.classe = 1
                selction_class = True
            elif epee_rect.collidepoint(event.pos) and game.background == 3:
                epee_affichee  = epee_grossie
                epee_affichee_rect = epee_grossie_rect
                game.classe = 2
                selction_class = True
            elif arc_rect.collidepoint(event.pos) and game.background == 3:
                arc_affichee  = arc_grossie
                arc_affichee_rect = arc_grossie_rect
                game.classe = 3
                selction_class = True
            elif bouclier_rect.collidepoint(event.pos) and game.background == 3:
                bouclier_affichee  = bouclier_grossie
                bouclier_affichee_rect = bouclier_grossie_rect
                game.classe = 4
                selction_class = True

    if game.background == 1 or 2 or 3 or 4:
        screen.blit(background, (0, 0))

    if game.background == 1:
        screen.blit(titre, titre_rect)
        screen.blit(play_affichee, play_affichee_rect)
        screen.blit(quit_buton, (quit_rect.x, quit_rect.y))  
    elif game.is_playing and game.background == 2:
        screen.blit(sexe_text, sexe_text_rect)
        screen.blit(female_affichee, female_affichee_rect)
        screen.blit(male_affichee, male_affichee_rect)
        screen.blit(valider_buton, valider_buton_rect)
        if selction_sex:
            screen.blit(valider_buton_affichee, valider_buton_affichee_rect)
        else:
            screen.blit(valider_buton_non, valider_buton_non_rect)
    elif game.is_playing and game.background == 3:
        screen.blit(class_text, class_text_rect)
        screen.blit(livre_affichee, livre_affichee_rect)
        screen.blit(epee_affichee, epee_affichee_rect)
        screen.blit(arc_affichee, arc_affichee_rect)
        screen.blit(bouclier_affichee, bouclier_affichee_rect)
        if selction_class:
            screen.blit(valider_buton_affichee, valider_buton_affichee_rect)
        else:
            screen.blit(valider_buton_non, valider_buton_non_rect)
    elif game.is_playing and game.background == 4:
        pygame.draw.rect(screen, (255, 255, 255), input_rect)
        rendered_text = font.render(text, True, text_color)
        screen.blit(rendered_text, input_rect)
        

    elif game.is_playing and game.background == 6:
        game.update(screen)

    pygame.display.update()