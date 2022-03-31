""""""

class Pieces():
    def __init__(self, x, y, type, team):
        self.__coords = (x, y)
        self.type = type
        self.team = team


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
        if xn > 5 :
            xn  = 5
        if yn > 5:
            yn = 5
        self.__coords = (xn, yn)



    def id(self):
        return 'P'

    def move(self):
        print("Choisissez votre mouvement :")
        print("avant, arrière, gauche, droite ?")
        move = input()

        if move == 'avant':
            if self.team  == "white":
                self.coords = (self.x -1, self.y)
            elif self.team == "black":
                self.coords = (self.x +1, self.y)

        elif move == 'arrière':
            if self.team  == "white":
                self.coords = (self.x +1, self.y)
            elif self.team == "black":
                self.coords = (self.x -1, self.y)

        elif move == 'droite':
            if self.team  == "white":
                self.coords = (self.x, self.y +1)
            elif self.team == "black":
                self.coords = (self.x, self.y -1)

        elif move == 'gauche':
            if self.team  == "white":
                self.coords = (self.x, self.y -1)
            elif self.team == "black":
                self.coords = (self.x, self.y +1)