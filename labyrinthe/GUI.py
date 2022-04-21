import turtle
import Graph as G
import Labyrinthe

WIDTH = 800
HEIGHT = 800

COLOR = 'white'


class GUI:
    def __init__(self) -> None:
        self.board = turtle.Turtle()
        turtle.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg=COLOR)
        turtle.up()
        # turtle.hideturtle()
        self.setOriginPosition()

    def showLabyrinthe(self, labyrinthe: G, nbLine: int, nbColumn: int, dist: float = 45):
        self.drawEdge(labyrinthe, nbLine, nbColumn, dist)
        self.drawLine(labyrinthe, nbLine, nbColumn, dist)
        self.drawColumn(labyrinthe, nbLine, nbColumn, dist)
        turtle.done()

    def drawLine(self, labyrinthe: G, nbLine: int, nbColumn: int, dist: float):
        for l in range(1, nbLine):
            turtle.up()
            turtle.setposition(-nbColumn*dist/2, (nbLine*dist/2) - l*dist)
            for c in range(1, nbColumn+1):
                turtle.up()
                if (l+1, c) not in labyrinthe.dico[(l, c)]:
                    turtle.down()
                turtle.forward(dist)
        turtle.up()

    def drawColumn(self, labyrinthe: G, nbLine: int, nbColumn: int, dist: float):
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

    def drawEdge(self, labyrinthe: G, nbLine: int, nbColumn: int, dist: float):
        turtle.setposition(-nbColumn*dist/2, -nbLine*dist/2)
        turtle.down()
        turtle.setposition(-nbColumn*dist/2, nbLine*dist/2)
        turtle.setposition(nbColumn*dist/2, nbLine*dist/2)
        turtle.setposition(nbColumn*dist/2, -nbLine*dist/2)
        turtle.setposition(-nbColumn*dist/2, -nbLine*dist/2)
        turtle.up()


    def setOriginPosition(self):
        turtle.home()

    # TODO écris moi la fonction dessin de la partie 2 :p


if __name__ == "__main__":
    GUI().showLabyrinthe(Labyrinthe.Labyrinthe, 4, 8)
