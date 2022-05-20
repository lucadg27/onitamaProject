import pieces
import table
import carte
import unittest

class Test_jeu(unittest.TestCase):

    def test_carte(self):
        a=1
        b=10
        main_une=table.Main('bleu',a,b)
        carte_une=carte.Carte(a,'bleu',main_une)
        carte_deux=carte.Carte(b,'bleu',main_une)

        self.assertEqual(carte_une.num, 1)
        self.assertEqual(carte_deux.num, 10)
        self.assertEqual(carte_une.team, 'bleu')
        self.assertEqual(carte_deux.car, "Singe")
        self.assertEqual(carte_deux.mouv_possible, [(- 1,- 1), (1,- 1), (1,1), (- 1,1)])
        self.assertEqual(carte_deux.main, main_une)


    def test_piece(self):
        table_une=table.Table()
        x_un=2
        y_un=3
        team='bleu'
        move=(1,1)
        piece_une=pieces.Piece(x_un,y_un,team,table_une)
        self.assertEqual(piece_une.coords, (2,3))
        self.assertEqual(piece_une.team, 'bleu')
        piece_une.move(move)
        self.assertEqual(piece_une.coords, (3, 4))
        self.assertEqual(piece_une.pv, 1)
        piece_une.kill()
        self.assertEqual(piece_une.pv, 0)


    def test_roi(self):

        table_une=table.Table()
        x_un=2
        y_un=3
        team='bleu'
        move=(1,1)
        piece_une=pieces.Roi(x_un,y_un,team,table_une)
        self.assertEqual(piece_une.coords, (2,3))
        self.assertEqual(piece_une.team, 'bleu')
        piece_une.move(move)
        self.assertEqual(piece_une.coords, (3, 4))
        self.assertEqual(piece_une.pv, 1)
        piece_une.kill()
        self.assertEqual(piece_une.pv, 0)



    def test_pion(self):

        table_une=table.Table()
        x_un=2
        y_un=3
        team='bleu'
        move=(1,1)
        piece_une=pieces.Pion(x_un,y_un,team,table_une)
        self.assertEqual(piece_une.coords, (2,3))
        self.assertEqual(piece_une.team, 'bleu')
        piece_une.move(move)
        self.assertEqual(piece_une.coords, (3, 4))
        self.assertEqual(piece_une.pv, 1)
        piece_une.kill()
        self.assertEqual(piece_une.pv, 0)







if __name__ == '__main__':

    unittest.main()