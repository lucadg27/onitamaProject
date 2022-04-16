

class Piece():
    """
    Cette classe gère les Pièces jouées pendant la partie.
    Deux sous-classes différencient les Rois et les Pions.
    """

    def __init__(self, x, y, team, table):
        """
        Génère une pièce d'une équipe donnée, à un emplacement donné sur le plateau.
        """
        self.__coords = (x, y)
        self.team = team
        self.pv = 1
        self.table = table


    @property
    def coords(self):
        return self.__coords

    @property
    def x(self):
        return self.coords[0]
    @property
    def y(self):
        return self.coords[1]

    @coords.setter
    def coords(self, new_coords):

        xn, yn = new_coords

        if xn > 4 :
            print("Vous ne pouvez pas sortir du plateau !")
            xn  = 4
        elif xn < 0:
            print("Vous ne pouvez pas sortir du plateau !")
            xn = 0

        if yn > 4:
            print("Vous ne pouvez pas sortir du plateau !")
            yn = 4
        elif yn < 0:
            print("Vous ne pouvez pas sortir du plateau !")
            yn = 0

        self.__coords = (xn, yn)


    def id(self):
        return 'Piece'

    def move(self, move):
        """
        Gère les mouvements possibles des pièces.
        Sur cette version, le jeu n'autorise que des mouvements simples (une pièce ne peut se déplacer que sur un case adjacente).
        Une pièce ne peut pas se déplacer sur une case occupée par une pièce alliée.
        Si une pièce se déplace sur une case occupée par une pièce adverse, elle mange cette pièce.
        """
        #TODO : lier les mouvements possibles aux cartes dans la main du joueur

        dx, dy = 0, 0

        if move == 'haut':
            dx -= 1
        elif move == 'bas':
            dx += 1
        elif move == 'droite':
            dy += 1
        elif move == 'gauche':
            dy -= 1

        for piece in self.table:
            if piece.coords == (self.x + dx, self.y + dy):
                if piece.team == self.team:
                    dx, dy = 0, 0
                    print("Erreur : vous tentez de vous déplacer sur une case déjà occupée par une de vos pièces !")
                    break
                else:
                    piece.kill()

        #Pas terrible de bouger après avoir tué une pièce potentiellement mangée. Mais plus compact...
        self.coords = (self.x + dx, self.y + dy)

    def car(self):
        return "0"

    def kill(self):
        """
        Permets à une pièce de se faire manger
        """
        self.pv = 0


class Roi(Piece):
    #Vérifier que la fonction est similaire à celle générale, sauf pour les deux derniers blocs
    def __init__(self, x, y, team, table):
        super().__init__(x, y, team, table)
        self.ptype = "Roi"

    def car(self):
        return "R"

    def kill(self):
        """
        Permets à un Roi de se faire manger.
        La particularité d'un Roi est que si il est mangé, le joueur adverse remporte la partie.
        """
        self.pv = 0
        if self.team == "Bleu":
            self.table.phase = "R won"
            print("Le Roi Bleu est mort : le joueur Rouge a gagné !")

        elif self.team == "Rouge":
            self.table.phase = "B won"
            print("Le Roi Rouge est mort : le joueur Bleu a gagné !")

    def move(self, move):
        """
        Gère les mouvements des pièces.
        Particularité du Roi : si il atteint l'autel adverse (case de laquelle commence le Roi adverse), la partie est gagnée.
        """
        #TODO : lier les mouvements possibles aux cartes dans la main du joueur

        dx, dy = 0, 0

        if move == 'haut':
            dx -= 1
        elif move == 'bas':
            dx += 1
        elif move == 'droite':
            dy += 1
        elif move == 'gauche':
            dy -= 1

        for piece in self.table:
            if piece.coords == (self.x + dx, self.y + dy):
                if piece.team == self.team:
                    dx, dy = 0, 0
                    print("Erreur : vous tentez de vous déplacer sur une case déjà occupée par une de vos pièces !")
                    break
                else:
                    piece.kill()

        #Pas terrible de bouger après avoir tué une pièce potentiellement mangée. Mais plus compact...
        self.coords = (self.x + dx, self.y + dy)

        if self.team == "Bleu" and self.coords == (0, 2):
            self.table.phase = "Victoire des Bleus"
            print("Le Roi Bleu a atteint l'Autel Rouge : le joueur Bleu gagne !")

        elif self.team == "Rouge" and self.coords == (4, 2):
            self.table.phase = "Victoire des Rouges"
            print("Le Roi Rouge a atteint l'Autel Bleu : le joueur Rouge gagne !")



class Pion(Piece):
    def __init__(self, x, y, team, table):
        super().__init__(x, y, team, table)
        self.ptype = "Pion"

    def car(self):
        return "P"
