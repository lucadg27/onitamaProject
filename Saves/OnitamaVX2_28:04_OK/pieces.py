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


    def move(self, move):
        #TODO : lier les mouvements possibles aux cartes dans la main du joueur

        dx, dy = move[0], move[1]

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
        self.pv = 0



class Roi(Piece):
    #Vérifier que la fonction est similaire à celle générale, sauf pour les deux derniers blocs
    def __init__(self, x, y, team, table):
        super().__init__(x, y, team, table)
        self.ptype = "Roi"

    def car(self):
        return "R"

    def kill(self):
        self.pv = 0
        if self.team == "Bleu":
            self.table.phase = "R won"
            print("Le Roi Bleu est mort : le joueur Rouge a gagné !")


        elif self.team == "Rouge":
            self.table.phase = "B won"
            print("Le Roi Rouge est mort : le joueur Bleu a gagné !")


    def move(self, move):
        #TODO : lier les mouvements possibles aux cartes dans la main du joueur

        dx, dy = move[0], move[1]

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
