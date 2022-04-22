import random as rd
'''
Ici nous nous affairerons à créer les cartes qui seront utilisées au cours de la partie.
Il existe 16 cartes, 5 d'entre elles seront piochées en début de partie et seront utilisées tout du long de celle-ci.
Les autres cartes sont mises de coté.
Parmis les cartes conservées, celles ci peuvent se trouver dans la main du joueur 1, dans la main du joueur 2 ou dans
la pioche qui a tout instant n'est composée que d'une carte.
Lorsqu'une carte est jouée elle est mise dans la pioche et la carte qui était déjà dans la pioche va dans la main
du joueur qui vient de jouer (leurs positions sont échangées).
Contrairement aux echecs, ce n'est pas le type de la pièce qui implique le délpacement mais la carte jouée par le jou eur.
Ainsi chaque carte permet de se déplacer d'une manière différente.
'''

dico = {1 : ["Crabe",[(0,- 2), (0, 2), (- 1, 0)]],
            2 : ["Cheval",[(0, - 1),  ( 1, 0), (- 1, 0)]],
            3 : ["Mante",[(- 1,- 1), (- 1,  1), (1, 0)]],
            4 : ["Oie",[(- 1, - 1), (1, 1), (0, - 1), (0, 1)]],
            5 : ["Sanglier", [(- 1, 0), (0,- 1), (0,1)]],
            6 : ["Tigre",[(- 2, 0), (1, 0)]],
            7 : ["Dragon",[(- 1,- 2), (- 1,2), (1,1), (1,- 1)]],
            8 : ["Grenouille",[(- 1,- 1), (0,- 2), (1,1)]],
            9 : ["Lapin",[(1,- 1), (- 1,1), (0, 2)]],
            10 : ["Singe", [(- 1,- 1), (1,- 1), (1,1), (- 1,1)]],
            11 : ["Elephant",[(0,- 1), (0,1), (- 1,1), (- 1,- 1)]],
            12 : ["Anguille",[(- 1, - 1), (1, - 1), (0, 1)]],
            13 : ["Cobra",[(0,- 1), (1,1), (- 1,1)]],
            14 : ["Boeuf",[(- 1,0), (1,0), (0,1)]],
            15 : ["Grue",[(- 1,0), (1,- 1), (1,1)]],
            16 : ["Coq",[(0,- 1), (0,1), (- 1,1),(1,- 1)]]}


def choix_carte():
    """
    Permet de choisir les 5 cartes utilisées tout du lond de la partie
    """

    deja_prise=[]

    for i in range (5):
        n=rd.randint(1,16)
        if n in deja_prise:
            i-=1
        else:
            deja_prise.append(n)

    return deja_prise


class Carte():
    """
    Définit les cartes utilisées pendant le jeu
    """
    def __init__(self, numero, team, main=None):
        self.num=numero
        self.mouvement=[]
        self.team=team
        self.main=main



        self.car = dico[self.num][0]
        self.mouv_possible = dico[self.num][1]

