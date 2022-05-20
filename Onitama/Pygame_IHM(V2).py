import pygame as p
from pygame.locals import(MOUSEBUTTONUP, K_ESCAPE, KEYDOWN, QUIT)

p.init()


#Dimensiions fenêtre
win_width = 1000
win_height = 700
screen = p.display.set_mode((win_width, win_height))
screen.fill((100,100,100))

n_row, n_col = 5, 5
sq_wid = 70
tab_i_off, tab_j_off = 100, 150


# Création échiquier
chess_board = []
is_white = False

for i in range(n_row):  # boucle sur les lignes
    chess_row = []
    for j in range(n_col):
        if (i + j) % 2 == 0:
            is_white = True
        else:
            is_white = False
        chess_row.append(is_white)
    chess_board.append(chess_row)

for i in range(5):
    for j in range(5):
        if chess_board[i][j]:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        p.draw.rect(screen, color, p.Rect(j * sq_wid + tab_j_off, i * sq_wid + tab_i_off, sq_wid, sq_wid))

        p.display.flip()


if __name__ == "main":
    running = True
    while running:
        for event in p.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if event.type == MOUSEBUTTONUP:
                pos = p.mouse.get_pos()

            elif event.type == QUIT:
                running = False





