import labyrinthe.Graph as G


if __name__ == "__main__":
    Labyrinthe = G.Graph()
    for i in range(1, 5):
        for j in range(1, 9):
            Labyrinthe.addNode((i, j))
    print(Labyrinthe)
