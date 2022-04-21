import Graph as G


#if __name__ == "__main__":
Labyrinthe = G.Graph()

for i in range(1, 5):           #création des noeuds du graphe
    for j in range(1, 9):
        Labyrinthe.addNode((i, j))
    
Labyrinthe.addEdge((1,1),(2,1)) #création des liens entre les noeuds du graphe
Labyrinthe.addEdge((2,1),(2,2))
Labyrinthe.addEdge((2,2),(2,3))
Labyrinthe.addEdge((2,2),(3,2))
Labyrinthe.addEdge((2,3),(1,3))
Labyrinthe.addEdge((1,3),(1,4))
Labyrinthe.addEdge((1,4),(1,5))
Labyrinthe.addEdge((1,4),(2,4))
Labyrinthe.addEdge((1,5),(2,5))
Labyrinthe.addEdge((2,4),(3,4))
Labyrinthe.addEdge((3,4),(3,5))
Labyrinthe.addEdge((2,5),(2,6))
Labyrinthe.addEdge((3,2),(4,2))
Labyrinthe.addEdge((4,2),(4,3))
Labyrinthe.addEdge((4,3),(4,4))
Labyrinthe.addEdge((1,6),(2,6))
Labyrinthe.addEdge((1,6),(1,7))
Labyrinthe.addEdge((1,7),(1,8))
Labyrinthe.addEdge((3,5),(3,6))
Labyrinthe.addEdge((3,6),(3,7))
Labyrinthe.addEdge((1,8),(2,8))
Labyrinthe.addEdge((2,6),(2,7))
Labyrinthe.addEdge((2,6),(3,6))
Labyrinthe.addEdge((2,7),(3,7))
Labyrinthe.addEdge((3,6),(4,6))
Labyrinthe.addEdge((4,5),(4,6))
Labyrinthe.addEdge((2,8),(3,8))
Labyrinthe.addEdge((3,8),(4,8))
Labyrinthe.addEdge((3,7),(4,7))
Labyrinthe.addEdge((4,7),(4,8))

print(Labyrinthe)
