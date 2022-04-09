# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import randint
import time
import matplotlib.pyplot as plt

# il est inutile d'importer Animal :
from pieces import Roi, Pion

"""
"""



class Table(list):
    """
    """

    def __init__(self):
        self.__plateau = [[0 for _ in range (5)] for _ in range (5)]

        self.append(Roi(4, 2, "Bleu", self))
        self.append(Pion(4, 0, "Bleu", self))
        self.append(Pion(4, 1, "Bleu", self))
        self.append(Pion(4, 3, "Bleu", self))
        self.append(Pion(4, 4, "Bleu", self))

        self.append(Roi(0, 2, "Rouge", self))
        self.append(Pion(0, 0, "Rouge", self))
        self.append(Pion(0, 1, "Rouge", self))
        self.append(Pion(0, 3, "Rouge", self))
        self.append(Pion(0, 4, "Rouge", self))

        self.phase = "playing"

        self.last_played = "Rouge"


    def case(self, x, y):
        return self.__plateau[x][y]

    def __str__(self):
        """
        """
        pos = {}
        for piece in self:
            pos[piece.coords] = piece.car()
        s = ""
        for i in range(5):
            for j in range(5):
                if (i, j) in pos:
                    s += pos[(i, j)]
                else:
                    s += "."
            s += "\n"
        return s


    def unRound(self, mode, team):
        """
        """
        #TODO : ajouter un choix de carte
        #TODO : changement de carte


        if mode == "PVP":
            if self.last_played == "Rouge" : self.coup("Bleu")
            elif self.last_played == "Bleu" : self.coup("Rouge")

        elif mode == "PVE":
            if team == "Bleu" :
                if self.last_played == "Rouge" : self.coup("Bleu")
                elif self.last_played == "Bleu" : self.coup_IA("Rouge")

            elif team == "Rouge" :
                if self.last_played == "Rouge" : self.coup_IA("Bleu")
                elif self.last_played == "Bleu" : self.coup("Rouge")


    def coup(self, joueur):
        print("Au tour des", joueur)
        print("Joueur", joueur, "choisissez une pièce à jouer")
        print("Entrez les coordonnées de la pièce voulue (type matrice) : ")
        i = int(input())
        j = int(input())
        coo = (i, j)

        check = False
        for piece in self:
            if piece.team == joueur and piece.coords == coo:
                print("Vous jouez le", piece.ptype, "en", coo)
                print("Choisissez votre mouvement :")
                print("haut, bas, gauche, droite (relatif au plateau)", "\n")
                move = input()
                piece.move(move)
                check = True
        if check == False: print("Erreur : pas de pièce trouvée !")

        table.clean()
        print(table)

        self.last_played = joueur

    def coup_IA(self, team):
        print("Au tour du joueur", team)
        print("*bip* *boup*")
        print("je suis un robot")

        pieces = []
        mouvements = ["haut", "bas", "droite", "gauche"]

        for piece in self:
            if piece.team == team:
                pieces.append(piece)

        n, k = randint(0, len(pieces)), randint(0, len(mouvements))
        piece_IA, move_IA = pieces[n], mouvements[k]
        print("HAL9000 joue le", piece_IA.ptype, "en", piece_IA.coords)
        print("Mouvement choisi :", move_IA)

        piece_IA.move(move_IA)

        table.clean()
        print(table)

        self.last_played = team


    def clean(self):
        for piece in self:
            if piece.pv == 0:
                self.remove(piece)


if __name__ == "__main__":
    table = Table()

    print("Choisissez le mode de jeu :")
    print("(PVP ou PVE)")
    mode = input()

    if mode == "PVE":
        print("Quelle couleur prenez-vous ?")
        print("Bleu ou Rouge")
        team = input() #Équipe du joueur principal
    else : team = "Bleu" #Par défaut. Variable inutile en PVP

    print("Les Bleus commencent, leurs pions sont en bas du plateau", '\n')
    print(table)

    while table.phase == "playing":
        table.unRound(mode, team)