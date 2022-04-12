class Graph:
    def __init__(self):
        self.dico = {}

    def __str__(self):
        return str(self.dico)

    def addNode(self, node: 'tuple[int]'):
        if node not in self.dico:
            self.dico[node] = []

    def addEdge(self, nodeA: 'tuple[int]', nodeB: 'tuple[int]'):
        self.dico[nodeA].append(nodeB)
        self.dico[nodeB].append(nodeA)

# TODO Écrire la documentation
