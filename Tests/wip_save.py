import pygame
from pygame.locals import(MOUSEBUTTONUP, K_ESCAPE, KEYDOWN, QUIT)

pygame.init()

#Dimensiions fenêtre
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Classe Tableau
class BoardSquare :
    def __init__(self, x_start, y_start, width_height, is_white):
        self.x_start = x_start
        self.y_start = y_start
        self.width_height = width_height
        self.is_white = is_white


#Calcul de coordonnées
def calculate_coordinates(x_array, y_array, is_white):
    #Fenêtre flexible : divise le côté le plus court en 8 pour créer les 8x8 cases
    if SCREEN_WIDTH < SCREEN_HEIGHT or SCREEN_WIDTH == SCREEN_HEIGHT: width_height = SCREEN_WIDTH / 8
    else: width_height = SCREEN_HEIGHT / 8

    #Calcul des coordonnées du coin haut gauche du carré considéré.
    #La multiplication place la coordonnée à [coordonnée matricielle du carré]*taille d'un carré
    x_coordinate = x_array * width_height
    y_coordinate = y_array * width_height

    return BoardSquare(x_coordinate, y_coordinate, width_height, is_white) #Retourne une case corrigée



#Création échiquier
chess_board = []
is_white = False

for y in range(8): #boucle sur les lignes
    chess_row = []
    is_white = not is_white #alternance couleurs. Première itération : case 0,0, blanche
    for x in range (8): #boucle sur les colonnes
        chess_row.append(calculate_coordinates(x, y, is_white))
        is_white = not is_white
    chess_board.append(chess_row)


for row in chess_board:
    for square in row:
        surf = pygame.Surface((square.width_height, square.width_height)) #Surface superposée au carré en question

        if square.is_white :
            surf.fill((255, 255, 255))
        else:
            surf.fill((0, 0, 0))

        #Dessin de la surface via Pygame
        rect = surf.get_rect()
        screen.blit(surf, (square.x_start, square.y_start))
        pygame.display.flip()


def get_square_for_position(pos): #renvoie le carré sélectionné par la souris
    for row in chess_board:
        if row[0].y_start < pos[1] < row[0].y_start + row[0].width_height: #limites de la colonne
            for square in row:
                if square.x_start < pos[0] < square.x_start + square.width_height: #limites en x du carré
                    return square

def highlight_selected_square(square):
    pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            highlight_selected_square(get_square_for_position(pos))

        elif event.type == QUIT:
            running = False

