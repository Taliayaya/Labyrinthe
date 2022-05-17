from time import sleep
import turtle
import labyrinthe.Graph as G
import labyrinthe.Labyrinthe as L
import queue

WIDTH = 800
HEIGHT = 800

BGCOLOR = 'white'
LLINECOLOR = 'black'
GLINECOLOR = 'blue'
FILLCOLOR = 'white'
VISITEDCOLOR = 'blue'
PATHCOLOR = 'green'


class GUI:
    u"""
    Classe permettant de représenter graphiquement un labyrinthe modélisé par un graphe et les différents sommets de ce graphe.

    Attributs:
    ----------
        self.board : turtle.Turtle
            Une fenêtre qui a comme dimensions WIDTH et HEIGHT, la largeur et la hauteur.

    Méthodes:
    ---------
        showLabyrinthe(self, labyrinthe: G, nbLine: int, nbColumn: int, dist: float = 45)
            Affiche le labyrinthe rentré en paramètre
            Attention, le nombre de lignes et de colonnes de ce labyrinthe doit également être précisé en paramètre.
            La largeur par défaut des cases est de 45 pixels

        drawGraph(self, labyrinthe: G, nbLine: int, nbColumn: int, dist: float = 45)
            Affiche le graphe utilisé pour décrire le labyrinthe de showLabyrinthe
    """

    def __init__(self) -> None:
        self.board = turtle.Turtle()
        turtle.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg=BGCOLOR)
        turtle.up()
        turtle.speed(0)
        self.coord = dict()
        turtle.hideturtle()
#        self.setOriginPosition()

    def showLabyrinthe(self, labyrinthe: 'G.Graph', nbLine: int, nbColumn: int, dist: float = 45):
        u"""
        Fonction permettant d'afficher le labyrinthe rentré en paramètre dans la fenêtre qui apparaît lors de l'appel de la classe
        Préconditions:
            labyrinthe : G.Graph
                Un objet de la classe graphe ayant des tuples en tant que sommets.
                C'est le labyrinthe affiché par la fonction.
            nbLine : int
                Le nombre de lignes de ce labyrinthe
            nbColumn : int
                Le nombre de colonnes de ce labyrinthe
            dist : float
                La largeur du côté des cases du labyrinthe

        Postconditions:
            Affiche la bordure du labyrinthe
            Affiche les murs horizontaux du labyrinthe
            Affiche les murs verticaux du labyrinthe
        """
        turtle.pencolor(LLINECOLOR)
        self.__drawFrame(nbLine, nbColumn, dist)
        self.__drawLine(labyrinthe, nbLine, nbColumn, dist)
        self.__drawColumn(labyrinthe, nbLine, nbColumn, dist)

    def __drawLine(self, labyrinthe: 'G.Graph', nbLine: int, nbColumn: int, dist: float):
        u"""
        Permet de dessiner les murs entre chaque ligne du labyrinthe

        Préconditions:
            labyrinthe : G.Graph
                Un objet de la classe graphe ayant des tuples en tant que sommets.
                C'est le labyrinthe affiché par la fonction.
            nbLine : int
                Le nombre de lignes de ce labyrinthe
            nbColumn : int
                Le nombre de colonnes de ce labyrinthe
            dist : float
                La largeur du côté des cases du labyrinthe

        Postconditions:
            Affiche les murs horizontaux du labyrinthe
        """
        for l in range(1, nbLine):
            turtle.up()
            turtle.setposition(-nbColumn*dist/2, (nbLine*dist/2) - l*dist)
            for c in range(1, nbColumn+1):
                turtle.up()
                if (l+1, c) not in labyrinthe.dico[(l, c)]:
                    turtle.down()
                turtle.forward(dist)
        turtle.up()

    def __drawColumn(self, labyrinthe: 'G.Graph', nbLine: int, nbColumn: int, dist: float):
        u"""
        Permet de dessiner les murs entre chaque colonne du labyrinthe

        Préconditions:
            labyrinthe : G.Graph
                Un objet de la classe graphe ayant des tuples en tant que sommets.
                C'est le labyrinthe affiché par la fonction.
            nbLine : int
                Le nombre de lignes de ce labyrinthe
            nbColumn : int
                Le nombre de colonnes de ce labyrinthe
            dist : float
                La largeur du côté des cases du labyrinthe

        Postconditions:
            Affiche les murs verticaux du labyrinthe
        """
        turtle.right(90)
        for c in range(1, nbColumn):
            turtle.up()
            turtle.setposition(-nbColumn*dist/2 + c*dist, (nbLine*dist/2))
            for l in range(1, nbLine+1):
                turtle.up()
                if (l, c+1) not in labyrinthe.dico[(l, c)]:
                    turtle.down()
                turtle.forward(dist)
        turtle.up()
        turtle.home()

    def __drawFrame(self, nbLine: int, nbColumn: int, dist: float):
        u"""
        Permet de dessiner la bordure du labyrinthe

        Préconditions:
            labyrinthe : G.Graph
                Un objet de la classe graphe ayant des tuples en tant que sommets.
                C'est le labyrinthe affiché par la fonction.
            nbLine : int
                Le nombre de lignes de ce labyrinthe
            nbColumn : int
                Le nombre de colonnes de ce labyrinthe
            dist : float
                La largeur du côté des cases du labyrinthe

        Postconditions:
            Affiche la bordure du labyrinthe
        """
        turtle.setposition(-nbColumn*dist/2, -nbLine*dist/2)
        turtle.down()
        turtle.setposition(-nbColumn*dist/2, nbLine*dist/2)
        turtle.setposition(nbColumn*dist/2, nbLine*dist/2)
        turtle.setposition(nbColumn*dist/2, -nbLine*dist/2)
        turtle.setposition(-nbColumn*dist/2, -nbLine*dist/2)
        turtle.up()

    def showGraph(self, labyrinthe: 'G.Graph', nbLine: int, nbColumn: int, dist: float = 45):
        u"""
        Fonction permettant d'afficher le graphe rentré en paramètre dans la fenêtre qui apparaît lors de l'appel de la classe
        Préconditions:
            labyrinthe : G.Graph
                Un objet de la classe graphe ayant des tuples en tant que sommets.
                C'est le graphe affiché par la fonction.
            nbLine : int
                Le nombre de lignes de ce graphe
            nbColumn : int
                Le nombre de colonnes de ce graphe
            dist : float
                La largeur du côté des cases du graphe

        Postconditions:
            Affiche les noeuds du graphe
            Affiche les arêtes horizontales du graphe
            Affiche les arêtes verticales du graphe
        """
        turtle.pencolor(GLINECOLOR)
        self.__drawHorizontalEdge(labyrinthe, nbLine, nbColumn, dist)
        self.__drawVerticalEdge(labyrinthe, nbLine, nbColumn, dist)
        self.__drawNode(nbLine, nbColumn, dist)

    def __drawHorizontalEdge(self, labyrinthe: 'G.Graph', nbLine: int, nbColumn: int, dist: float):
        u"""
        Permet de dessiner les arêtes horizontales du graphe

        Préconditions:
            labyrinthe : G.Graph
                Un objet de la classe graphe ayant des tuples en tant que sommets.
                C'est le graphe affiché par la fonction.
            nbLine : int
                Le nombre de lignes de ce graphe
            nbColumn : int
                Le nombre de colonnes de ce graphe
            dist : float
                La largeur du côté des cases du graphe

        Postconditions:
            Affiche les arêtes horizontales du graphe
        """
        for l in range(1, nbLine+1):
            turtle.up()
            turtle.setposition(-nbColumn*dist/2 + 0.5*dist,
                               (nbLine*dist/2) - l*dist + 0.5*dist)
            for c in range(1, nbColumn):
                turtle.up()
                if (l, c+1) in labyrinthe.dico[(l, c)]:
                    turtle.down()
                turtle.forward(dist)
        turtle.up()

    def __drawVerticalEdge(self, labyrinthe: 'G.Graph', nbLine: int, nbColumn: int, dist: float):
        u"""
        Permet de dessiner les arêtes verticales du graphe

        Préconditions:
            labyrinthe : G.Graph
                Un objet de la classe graphe ayant des tuples en tant que sommets.
                C'est le graphe affiché par la fonction.
            nbLine : int
                Le nombre de lignes de ce graphe
            nbColumn : int
                Le nombre de colonnes de ce graphe
            dist : float
                La largeur du côté des cases du graphe

        Postconditions:
            Affiche les arêtes verticales du graphe
        """
        turtle.right(90)
        for c in range(1, nbColumn+1):
            turtle.up()
            turtle.setposition(-nbColumn*dist/2 + c*dist -
                               0.5*dist, (nbLine*dist/2) - 0.5*dist)
            for l in range(1, nbLine):
                turtle.up()
                if (l+1, c) in labyrinthe.dico[(l, c)]:
                    turtle.down()
                turtle.forward(dist)
        turtle.up()
        turtle.home()

    def __drawNode(self, nbLine: int, nbColumn: int, dist: int):
        u"""
        Permet de dessiner les noeuds du graphe

        Préconditions:
            labyrinthe : G.Graph
                Un objet de la classe graphe ayant des tuples en tant que sommets.
                C'est le graphe affiché par la fonction.
            nbLine : int
                Le nombre de lignes de ce graphe
            nbColumn : int
                Le nombre de colonnes de ce graphe
            dist : float
                La largeur du côté des cases du graphe

        Postconditions:
            Affiche les noeuds du graphe
        """
        self.coord["dist"] = dist
        turtle.fillcolor(FILLCOLOR)
        for l in range(1, nbLine+1):
            turtle.up()
            x = -nbColumn*dist/2 + 0.5*dist
            y = (nbLine*dist/2) - l*dist + 0.25*dist
            turtle.goto(x, y)
            for c in range(1, nbColumn+1):
                # print(x, y)
                turtle.down()
                turtle.begin_fill()
                self.coord[(l, c)] = turtle.pos()
                turtle.circle(dist/4)
                turtle.end_fill()
                turtle.up()
                turtle.forward(dist)
        turtle.up()
        # print(self.coord)

    def drawParcours(self, labyrinthe: 'G.Graph', dist: float = 45):
        u"""
        Permet de dessiner les noeuds du graphe parcourus lors d'un parcours en profondeur du graphe en partant du noeud (1, 1)

        Préconditions:
            labyrinthe : G.Graph
                Un objet de la classe graphe ayant des tuples en tant que sommets.
                C'est le graphe affiché par la fonction.
            nbLine : int
                Le nombre de lignes de ce graphe
            nbColumn : int
                Le nombre de colonnes de ce graphe
            dist : float
                La largeur du côté des cases du graphe

        Postconditions:
            Affiche les noeuds du graphe parcourus lors d'un parcours en profondeur du graphe en partant du noeud (1, 1)
        """
        labyrinthe.dfs_recursif((1, 1))
        for l, c in labyrinthe.vus:
            x, y = self.coord[(l, c)]
            turtle.goto(x, y)
            turtle.fillcolor(VISITEDCOLOR)
            turtle.begin_fill()
            turtle.circle(dist/4)
            turtle.end_fill()
            turtle.up()
            sleep(0.2)
        turtle.up()

    def showChemin(self, labyrinthe: 'G.Graph'):
        u"""
        Permet de tracer le chemin pour aller du départ à l'arrivée

        Précondition:
            labyrinthe : G.Graph
                l'instance du labyrinthe à dessiner

        Postcondition:
            Trace au feutre rouge le trajet du début (1,1) à la sortie (4,8) par exemple
        """
        node = (4, 8)
        coord = self.coord[(1, 1)]

        # Crée une pile pour inverser le trajet
        pile = queue.LifoQueue()
        pile.put(node)
        turtle.goto(coord)
        turtle.pencolor('red')
        turtle.pensize(2)
        turtle.pendown()
        # Remplit la pile des enfant -> parent pour obtenir parent -> enfant
        while node is not None:
            node = labyrinthe.parent[node]
            pile.put(node)

        # On retire le parent initial (1, 1)
        pile.get()

        # On trace le chemin en dépilant
        while not pile.empty():
            node = pile.get()
            print(node)
            coordx, coordy = self.coord[node]
            turtle.goto((coordx, coordy + (self.coord["dist"]/4)))
            sleep(0.2)
        turtle.penup()


if __name__ == "__main__":
    test = GUI()
    labyrinthe = L.Labyrinthe
    test.showLabyrinthe(labyrinthe, 4, 8)
    test.showGraph(labyrinthe, 4, 8)
    test.drawParcours(labyrinthe)
    test.showChemin(labyrinthe)
    turtle.done()
