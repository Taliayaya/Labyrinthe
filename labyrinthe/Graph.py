class Graph:
    u"""
    Classe permettant de représenter un labyrinthe ainsi
    que ses embranchements sous la forme d'un graphe.

    Attributs:
    ----------
        dico : dict[list[tuple[int, int]]]
            Un dictionnaire qui, pour chaque clé correspondant au point, sous
            la forme d'un tuple x, y, associe une liste qui contient les points
            auquel il est relié. Ces points sont eux aussi formés de tuple x, y en int.

    Méthodes:
    ---------
        addNode(node : tuple[int, int])
            Ajoute au dictionnaire du graphe une nouvelle clef correspondant
            au tuple x, y s'il n'existe pas.

        addEdge(nodeA : tuple[int, int], nodeB: tuple[int, int])
            Ajoute une liaison entre le noeud A et le noeud B,
            en ajoutant dans la liste à clé A et B la valeur
            B et A.
    """

    def __init__(self) -> None:
        u"""
        Fonction permettant de créer un graphe

        Préconditions:
            Nom du graphe (self)

        Postconditions:
            Crée le graphe sous forme d'un dictionnaire
        """
        self.dico = dict()
        self.parent = dict()
        self.parent[(1, 1)] = None

    def __str__(self) -> str:
        u"""
        Fonction permettant l'affichage sous forme de dictionnaire du graphe

        Préconditions:
            Nom du graphe (self)

        Postconditions:
            Contenu du graphe (self.graphe)
        """
        return str(self.dico)

    def addNode(self, node: 'tuple[int]') -> None:
        u"""
        Permet d'ajouter un noeud dans le graphe

        Précondition:
            node : tuple[int, int]
                Est le nom du sommet à ajouter au graphe

        Postcondition:
            Ajoute le noeud au graphe, dans le dictionnaire
            de l'instance.
        """
        if node not in self.dico:
            self.dico[node] = []

    def addEdge(self, nodeA: 'tuple[int, int]', nodeB: 'tuple[int, int]') -> None:
        u"""
        Permet d'ajouter une liaison entre le noeud A et le noeud B

        Préconditions:
            nodeA : tuple[int, int]
                L'un des deux noeuds de la liaison à effectuer

            nodeB : tuple[int, int]
                L'un des deux noeuds de la liaisons à effectuer 

        Postcondition:
            Ajoute la liaison au dictionnaire des noeuds dans leur liste
            d'adjacences respectives
        """
        self.dico[nodeA].append(nodeB)
        self.dico[nodeB].append(nodeA)

    def dfs_recursif(self, node: 'tuple[int, int]', reset=True) -> list:
        u"""Parcours un graphe de façon récursive en profondeur

        Précondition:
            node :  tuple[int, int] 
                est le nom de sommet de départ
            reset : (bool) 
                permet de réinitialiser la liste des sommets parcourus

        Postcondition:
            Remplie un dictionnaire des parents et une liste des noeuds visités
        """
        if reset:
            self.vus = []
        # print(node)
        self.vus.append(node)
        nextNodes = self.dico[node]
        for nNode in nextNodes:
            if nNode not in self.vus:
                self.parent[nNode] = node
                self.dfs_recursif(nNode, False)

    def passage(self, nodeA: 'tuple[int, int]', nodeB: 'tuple[int, int]') -> bool:
        u"""
        Vérifie si les noeuds A et B sont conjoints
        et qu'une liaison existe entre les deux.

        Préconditions:
            nodeA : tuple[int, int]
                Le premier noeud à vérifier
            nodeA : tuple[int, int]
                Le second noeud à vérifier

        Postcondition:
            Renvoie un booléen signifiant si les noeuds sont liés ou non
        """
        return (nodeA in self.dico[nodeB]
                and nodeB in self.dico[nodeA])
