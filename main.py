import pygame
from game import Game
from image import *

pygame.init()
pygame.display.set_caption("Tower of the Arcane Realms")

game = Game()
running = True

while running:
    
    if game.background == 1 or 2:
        screen.blit(background, (0, 0))

    if game.is_playing and game.background == 3:
        game.update(screen)
    elif game.is_playing and game.background == 2:
        screen.blit(male, (male_rect.x, male_rect.y) )
        screen.blit(female, (female_rect.x, female_rect.y))
        
        screen.blit(female_affichee, female_affichee_rect)
        screen.blit(male_affichee, male_affichee_rect)
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

        elif event.type == pygame.MOUSEMOTION:
            if female_rect.collidepoint(event.pos):
                female_affichee = female_grossie
                female_affichee_rect = female_grossie_rect
            else:
                female_affichee = female
                female_affichee_rect = female_rect

            if male_rect.collidepoint(event.pos):
                male_affichee = male_grossie
                male_affichee_rect = male_grossie_rect
            else:
                male_affichee = male
                male_affichee_rect = male_rect


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