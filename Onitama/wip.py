import pygame as p
from pygame.locals import(MOUSEBUTTONUP, K_ESCAPE, KEYDOWN, QUIT)

import numpy as np
from numpy.random import randint
import numpy.random as nr

from table import Table, Main, Pioche

team = "Bleu"

p.init()
p.font.init()

#Couleurs
WHITE = (240, 240, 240)
BLACK = (200, 200, 200)
BROWN = (100, 50, 0)


#Dimensions IHM
screen_height = 750
screen_width = 1000


n_row, n_col = 5, 5
sq_wid = (screen_height/2)/n_row
j_off, i_off = screen_width/10, screen_height/4

board_width, board_height = 5*sq_wid + 20, 5*sq_wid + 20
card_width, card_height = sq_wid, 1.618*sq_wid


#Création fenêtre
screen = p.display.set_mode((screen_width, screen_height))
screen.fill((250,250,250))
p.display.set_caption("Onitama")



def set_background():

    #Cadre d'échiquier
    p.draw.rect(screen, BROWN, p.Rect((j_off-10, i_off-10), (board_width, board_height)))

    #Cadre cartes
    p.draw.rect(screen, BROWN, p.Rect((j_off + 0.5*board_width - 1.5*card_width, i_off - card_height - 25),
                                      (card_width, card_height)))
    p.draw.rect(screen, BROWN, p.Rect((j_off + 0.5*board_width + 0.5*card_width, i_off - card_height - 25),
                                      (card_width, card_height)))

    p.draw.rect(screen, BROWN, p.Rect((j_off + 0.5*board_width - 1.5*card_width, i_off + board_height + 25),
                                      (card_width, card_height)))
    p.draw.rect(screen, BROWN, p.Rect((j_off + 0.5*board_width + 0.5*card_width, i_off + board_height + 25),
                                      (card_width, card_height)))

    p.draw.rect(screen, BROWN, p.Rect((j_off + board_width + 0.7*card_width, i_off + 0.5*board_height - 0.5*card_height),
                                      (card_width, card_height)))


    ##Création échiquier
    chess_board = []
    is_white = False

    #Remplissage chess_board
    for i in range(n_row):
        chess_row = []
        for j in range(n_col):
            is_white = not is_white
            chess_row.append(is_white)

        chess_board.append(chess_row)

    #Affichage carrés
    for i in range(n_row):
        for j in range(n_col):
            if chess_board[i][j] : color = WHITE
            else: color = BLACK
            p.draw.rect(screen, color, p.Rect(j*sq_wid + j_off, i*sq_wid + i_off, sq_wid, sq_wid))
            p.display.flip()





def show_txt(txt): #TODO : affichage utile et estéthique
    #Création objets
    font = p.font.SysFont('helveticaneue', 15)
    txt_img = font.render(txt, True, BLACK)
    txt_rect = txt_img.get_rect() #TODO : remplacer par un rectangle normal, placé au bon endroit par rapport au texte
    txt_rect.center = (0.8*screen_width, 0.2*screen_height)

    #Affichage
    p.draw.rect(screen, BROWN, txt_rect)
    screen.blit(txt_img, txt_rect)
    p.display.update()


def case_coordinates(x, y):
    return (x-i_off)//board_height, (y-j_off)//board_width


def choix_piece(x, y, table, team):
    case = case_coordinates(x, y)
    piece_valide, carte_valide = None, None

    #Choix Piece
    for piece in table:
        if (piece.coords == case) and (piece.team == team): piece_valide = piece
        #else : print("ERROR : Case choisie ne contient pas une pièce de votre équipe") #Pas nécessaire ? Juste de rien faire

    return piece_valide


def choix_carte(x, y, team):
    #Choix Carte
    choix_carte = 0
    carte_valide = None

    coords_cartes = [[j_off + 0.5*board_width - 1.5*card_width, i_off - card_height - 25],
                     [j_off + 0.5*board_width + 0.5*card_width, i_off - card_height - 25],
                     [j_off + 0.5*board_width - 1.5*card_width, i_off + board_height + 25],
                     [j_off + 0.5*board_width + 0.5*card_width, i_off + board_height + 25],
                     [j_off + board_width + 0.7*card_width, i_off + 0.5*board_height - 0.5*card_height]]

    for carte in coords_cartes:
        if (carte[0] < x < carte[0]+card_height) and (carte[1] < y < carte[1]+card_width):
            choix_carte = carte

    if team == "Bleu":
        if choix_carte == 3: carte_valide = main_bleue[0]
        elif choix_carte == 4: carte_valide = main_bleue[1]
    elif team == "Rouge":
        if choix_carte == 1: carte_valide = main_rouge[0]
        elif choix_carte == 2: carte_valide = main_rouge[1]
    else : print("ERROR")

    return carte_valide



def chosen(x, y, carte_valide, piece_valide):
    #Une fois le choix fait
    cases_possibles = []

    if carte_valide != None and piece_valide != None:
        for mouv in carte_valide.mouv_possible:
            cases_possibles.append( [piece_valide.coords[0] + mouv[0], piece_valide.coords[1] + mouv[1]] )

    case = case_coordinates(x, y)
    if case in cases_possibles:
        piece_valide.coords = case





if __name__ == "__main__":

    #Création instances
    table = Table()
    l_carte = nr.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 5, replace=False)
    main_bleue = Main('blue', l_carte[0], l_carte[1])
    main_rouge = Main('red', l_carte[2], l_carte[3])
    pioche = Pioche('pioche', l_carte[4])

    team = "Bleu"


    #Affichage
    set_background()

    running = True
    while running:
        for event in p.event.get():

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONUP:
                (x_pos, y_pos) = p.mouse.get_pos()






