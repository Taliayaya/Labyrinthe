import labyrinthe.Labyrinthe as L
import labyrinthe.Graph as G
import unittest


class BasicTests(unittest.TestCase):
    u"""
    Effectue des tests basiques pour vérifier que les fonctions
    respectent leur rôle
    """

    def test_passage(self):
        u"""
        Vérifie que l'on peut bien passer ou non des cases A à B
        sur différents noeuds 
        """
        # Preparing test
        test_labyrinthe = L.Labyrinthe
        data = [[(1, 2), (2, 2)], [(2, 2), (2, 3)], [(2, 2), (3, 3)],
                [(2, 2), (2, 2)], [(2, 3), (2, 5)]]

        # Running test
        test_results = [test_labyrinthe.passage(A, B) for A, B in data]

        # Test results
        expected_results = [False, True, False, False, False]
        self.assertListEqual(test_results, expected_results)

    def test_nodeCreationEmpty(self):
        u"""
        Vérifie si l'ajout d'un noeud dans un graphe fonctionne
        """
        # Preparing test
        test_graph = G.Graph()

        # Running test
        test_graph.addNode((1, 1))
        test_graph.addNode((4, 8))

        # Test Result
        test_result = test_graph.dico
        expected_result = {(1, 1): [], (4, 8): []}
        self.assertDictEqual(test_result, expected_result)

    def test_nodeCreationNotEmpty(self):
        u"""
        Vérifie si l'ajout d'un noeud qui existe déjà dans un graphe
        n'écrase pas l'actuel
        """
        # Preparing test
        test_graph = G.Graph()
        test_graph.addNode((1, 1))
        test_graph.addNode((4, 8))
        test_graph.addEdge((1, 1), (4, 8))

        # Running test
        test_graph.addNode((4, 8))

        # Test Result
        test_result = test_graph.dico[(4, 8)]
        expected_result = [(1, 1)]
        self.assertListEqual(test_result, expected_result)

    def test_addEdge(self):
        u"""
        Une liaison entre les deux noeuds devrait se créer
        """
        # Preparing test
        test_graph = G.Graph()
        test_graph.addNode((1, 1))
        test_graph.addNode((4, 8))

        # Running test
        test_graph.addEdge((1, 1), (4, 8))

        # Test Result
        test_result_1 = test_graph.dico[(1, 1)]
        test_result_2 = test_graph.dico[(4, 8)]
        expected_result_1 = [(4, 8)]
        expected_result_2 = [(1, 1)]
        self.assertListEqual(test_result_1, expected_result_1)
        self.assertListEqual(test_result_2, expected_result_2)


unittest.main(verbosity=2)
