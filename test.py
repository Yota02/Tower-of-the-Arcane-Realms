import pygame

pygame.init()

# définir la fenêtre
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Champ de saisie")

# définir la police de caractères
font = pygame.font.Font(None, 32)

# définir la couleur du texte et du fond
text_color = (0, 0, 0)
bg_color = (255, 255, 255) 

# définir le rectangle de la zone de saisie
input_rect = pygame.Rect(50, 50, 200, 32)

# définir le texte par défaut
text = ""

# boucle principale
while True:
    # gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # action à effectuer lorsqu'on appuie sur Entrée
                print(text)
                text = ""
            elif event.key == pygame.K_BACKSPACE:
                # supprimer le dernier caractère du texte
                text = text[:-1]
            else:
                # ajouter le caractère à la fin du texte
                text += event.unicode
    
    # dessiner le fond
    screen.fill(bg_color)
    
    # dessiner la zone de saisie
    pygame.draw.rect(screen, text_color, input_rect, 2)
    
    # afficher le texte dans la zone de saisie
    input_text = font.render(text, True, text_color)
    screen.blit(input_text, (input_rect.x + 5, input_rect.y + 5))
    
    # actualiser l'écran
    pygame.display.update()
