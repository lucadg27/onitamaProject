import pygame
from pygame.locals import(MOUSEBUTTONUP, K_ESCAPE, KEYDOWN, QUIT)

pygame.init()

#Dimensiions fenêtre
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

row, col = 5, 5

#Classe Tableau
class BoardSquare :
    def __init__(self, x_start, y_start, width_height, is_white):
        self.x_start = x_start
        self.y_start = y_start
        self.width_height = width_height
        self.is_white = is_white



#Création échiquier
is_white = True
sq_width = 50

x_off = 50
y_off = 50

chess_board = []

for i in range(row): #boucle sur les lignes
    row = []
    is_white = not is_white
    for j in range (col): #boucle sur les colonnes
        is_white = not is_white

        if is_white : color = (255, 255, 255)
        else : color = (0, 0, 0)






for row in chess_board:
    for square in row:
        surf = pygame.Surface((square.sq_width, square.sq_width)) #Surface superposée au carré en question

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

