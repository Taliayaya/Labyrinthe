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
    def __init__(self):
        self.dico = {}

    def __str__(self):
        return str(self.dico)

    def addNode(self, node: 'tuple[int, int]'):
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

    def addEdge(self, nodeA: 'tuple[int, int]', nodeB: 'tuple[int, int]'):
        u"""
        Permet d'ajouter une liaison entre le noeud A et le noeud B

        Préconditions:
            nodeA : tuple[int, int]
                L'un des deux noeuds de la liaison à effectuer
            
            nodeB : tuple[int int]
                L'un des deux noeuds de la laisons à effectuer 

        Postcondition:
            Ajoute la liaison au dictionaire des noeuds dans leur liste
            d'adjacences respectives
        """
        self.dico[nodeA].append(nodeB)
        self.dico[nodeB].append(nodeA)

# TODO Écrire la documentation
