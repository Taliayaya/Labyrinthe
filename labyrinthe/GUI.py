import turtle
import labyrinthe.Graph as G
import labyrinthe.Labyrinthe as L

WIDTH = 800
HEIGHT = 800

COLOR = 'white'


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

        drawGraph()
            méthode à implémenter
    """
    def __init__(self) -> None:
        self.board = turtle.Turtle()
        turtle.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg=COLOR)
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
        self.__drawEdge(labyrinthe, nbLine, nbColumn, dist)
        self.__drawLine(labyrinthe, nbLine, nbColumn, dist)
        self.__drawColumn(labyrinthe, nbLine, nbColumn, dist)
        turtle.done()

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

    def showGraph(self, labyrinthe: 'G.Graph', nbLine: int, nbColumn: int, dist: float):
        pass



if __name__ == "__main__":
    GUI().showLabyrinthe(Labyrinthe.Labyrinthe, 4, 8)
