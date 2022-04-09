""""""

class Piece():
    def __init__(self, x, y, team, table):
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

    def move(self):
        #TODO : lier les mouvements possibles aux cartes dans la main du joueur
        #TODO : s'assurer de ne pas sortir du plateau (contrainte dans le coord setter insuffisante)
        #TODO : s'assurer que deux pièces ne se chevauchent pas AVANT de bouger
        print("Choisissez votre mouvement :", '\n')
        print("haut, bas, gauche, droite  - relatif au plateau")
        move = input()

        if move == 'haut':
            self.coords = (self.x -1, self.y)
        elif move == 'bas':
            self.coords = (self.x +1, self.y)
        elif move == 'droite':
            self.coords = (self.x, self.y +1)
        elif move == 'gauche':
            self.coords = (self.x, self.y -1)
        for piece in self.table:
            if piece.team != self.team and piece.coords == self.coords:
                piece.kill()

    def car(self):
        return "0"

    def kill(self):
        self.pv = 0



class Roi(Piece):
    def __init__(self, x, y, team, table):
        super().__init__(x, y, team, table)
        self.ptype = "Roi"

    def car(self):
        return "R"

    def kill(self):
        self.pv = 0
        if self.team == "B":
            self.table.phase = "R won"
            print("Le Roi Bleu est mort : le joueur Rouge a gagné !")

        elif self.team == "R":
            self.table.phase = "B won"
            print("Le Roi Rouge est mort : le joueur Bleu a gagné !")


class Pion(Piece):
    def __init__(self, x, y, team, table):
        super().__init__(x, y, team, table)
        self.ptypee = "Pion"

    def car(self):
        return "P"
