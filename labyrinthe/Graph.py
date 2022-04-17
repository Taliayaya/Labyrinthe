class Graph:           # Classe permettant d'implémenter un graphe avec un dictionnaire de listes
    def __init__(self)->None:
        u"""
        Fonction permettant de créer un graphe

        Préconditions:
            Nom du graphe (self)
        
        Postconditions:
            Aucune
        """
        self.dico = {}

    def __str__(self)->str:
        u"""
        Fonction permettant l'affichage sous forme de dictionnaire du graphe

        Préconditions:
            Nom du graphe (self)
        
        Postconditions:
            Contenu du gtraphe (self.graphe)
        """
        return str(self.dico)

    def addNode(self, node: 'tuple[int]')->None:
        u"""
        Fonction qui permet d'ajouter un noeud dans le graphe
        
        Préconditions:
            Nom du graphe (self) et nom du noeud à ajouter
        
        Postconditions:
            Aucune
        """
        if node not in self.dico:
            self.dico[node] = []

    def addEdge(self, nodeA: 'tuple[int]', nodeB: 'tuple[int]')->None:
        u"""
        Fonction qui permet d'ajouter une arête dans le graphe entre deux sommets
        
        Préconditions:
            Nom du graphe (self) et noms des noeuds à relier
        
        Postconditions:
            Aucune
        """
        self.dico[nodeA].append(nodeB)
        self.dico[nodeB].append(nodeA)
