import pygame
import pygame.locals

pygame.init()
pygame.font.init()

ecran = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Jeu DÉSpéche-toi")

image = pygame.image.load("d1.jpg").convert()

pygame.display.set_icon(image)

fond = pygame.image.load("fond3.jpg")
fond = fond.convert()

taille_fond = (600, 600)
fond = pygame.transform.scale(fond, taille_fond)

# Configuration du texte
text = "DÉSpéche-toi"
text1 = "Jouer"
font = pygame.font.Font(None, 78)
font1 = pygame.font.Font(None, 68)
text_surface = font.render(text, True, (57, 0, 97))
text_position = (ecran.get_width() // 2 - text_surface.get_width() // 2, ecran.get_height() // 4 - text_surface.get_height() // 2)

# Fonction pour créer un bouton
def create_button(x, y, w, h, text1, text1_color, action=None):
    pygame.draw.rect(ecran, (0, 0, 0), (x, y, w, h))
    pygame.draw.rect(ecran, (0, 0, 0), (x, y, w, h), 2)
    text1_surface = font1.render(text1, True, text1_color)
    text1_position = (x + w // 2 - text1_surface.get_width() // 2, y + h // 2 - text1_surface.get_height() // 2)
    ecran.blit(text1_surface, text1_position)
    if action is not None:
        return action

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    ecran.blit(fond, (0,0))
    ecran.blit(text_surface, text_position)
    create_button(ecran.get_width() // 2 - 100, ecran.get_height() // 1.3, 200, 60, "JOUER", (57, 0, 97), pygame.quit)
    pygame.display.flip()

pygame.quit()