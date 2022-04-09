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

        self.append(Roi(4, 2, "B", self))
        self.append(Pion(4, 0, "B", self))
        self.append(Pion(4, 1, "B", self))
        self.append(Pion(4, 3, "B", self))
        self.append(Pion(4, 4, "B", self))

        self.append(Roi(0, 2, "R", self))
        self.append(Pion(0, 0, "R", self))
        self.append(Pion(0, 1, "R", self))
        self.append(Pion(0, 3, "R", self))
        self.append(Pion(0, 4, "R", self))

        self.phase = "playing"


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


    def unTour(self, team):
        """
        """
        #TODO : ajouter un choix de carte
        #TODO : changement de carte
        #TODO : différencier le tour des deux équipes (IA ? PVP ?)

        print("Quelle pièce jouer ?", '\n')
        print("Entrer coordonnées ; type matrice : (ligne, colonne)")
        i = int(input())
        j = int(input())
        coo = (i, j)

        check = False
        for piece in self:
            if piece.coords == coo:
                piece.move()
                check = True
                #TODO : ajouter une erreur si aucune pièce n'est trouvée (ou si deux se chevauchent)
        if check == False:
            print("erreur : pas de pièce trouvée")

        table.clean()

        print(table)

    def clean(self):
        for piece in self:
            if piece.pv == 0:
                self.remove(piece)


if __name__ == "__main__":
    table = Table()
    team = "B"
    print("Vous jouez les ", team, '\n')
    print("Vos pions sont en bas du plateau")

    print(table)

    while table.phase == "playing":
        table.unTour("B")

