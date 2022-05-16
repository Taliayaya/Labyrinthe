import turtle
import labyrinthe.Graph as G
import labyrinthe.Labyrinthe as L

WIDTH = 800
HEIGHT = 800

BGCOLOR = 'white'
LLINECOLOR = 'black'
GLINECOLOR = 'blue'
FILLCOLOR = 'white'
VISITEDCOLOR = 'blue'


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
        # turtle.hideturtle()
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
        self.__drawFrame(labyrinthe, nbLine, nbColumn, dist)
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

    def __drawFrame(self, labyrinthe: 'G.Graph', nbLine: int, nbColumn: int, dist: float):
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
        self.__drawNode(labyrinthe, nbLine, nbColumn, dist)

    def __drawHorizontalEdge(self, labyrinthe, nbLine, nbColumn, dist):
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
            turtle.setposition(-nbColumn*dist/2 + 0.5*dist, (nbLine*dist/2) - l*dist + 0.5*dist)
            for c in range(1, nbColumn):
                turtle.up()
                if (l, c+1) in labyrinthe.dico[(l, c)]:
                    turtle.down()
                turtle.forward(dist)
        turtle.up()

    def __drawVerticalEdge(self, labyrinthe, nbLine, nbColumn, dist):
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
            turtle.setposition(-nbColumn*dist/2 + c*dist - 0.5*dist, (nbLine*dist/2) - 0.5*dist)
            for l in range(1, nbLine):
                turtle.up()
                if (l+1, c) in labyrinthe.dico[(l, c)]:
                    turtle.down()
                turtle.forward(dist)
        turtle.up()
        turtle.home()

    def __drawNode(self, labyrinthe, nbLine, nbColumn, dist):
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
        turtle.fillcolor(FILLCOLOR)
        for l in range(1, nbLine+1):
            turtle.up()
            turtle.setposition(-nbColumn*dist/2 + 0.5*dist, (nbLine*dist/2) - l*dist + 0.25*dist)
            for c in range(1, nbColumn+1):
                turtle.down()
                turtle.begin_fill()
                turtle.circle(dist/4)
                turtle.end_fill()
                turtle.up()
                turtle.forward(dist)
        turtle.up()

    def drawParcours(self, labyrinthe: 'G.Graph', nbLine, nbColumn, dist = 45):
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
        for l in range(1, nbLine+1):
            turtle.up()
            turtle.setposition(-nbColumn*dist/2 + 0.5*dist, (nbLine*dist/2) - l*dist + 0.25*dist)
            for c in range(1, nbColumn+1):
                turtle.down()
                if (l, c) in labyrinthe.dfs_recursif((1, 1)):
                    turtle.fillcolor(VISITEDCOLOR)
                else:
                    turtle.fillcolor(FILLCOLOR)
                turtle.begin_fill()
                turtle.circle(dist/4)
                turtle.end_fill()
                turtle.up()
                turtle.forward(dist)
        turtle.up()

if __name__ == "__main__":
    test = GUI()
    test.showLabyrinthe(L.Labyrinthe, 4, 8)
    test.showGraph(L.Labyrinthe, 4, 8)
    test.drawParcours(L.Labyrinthe, 4, 8)
    turtle.done()
