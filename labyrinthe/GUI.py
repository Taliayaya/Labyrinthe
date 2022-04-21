import turtle

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

    def showLabyrinthe(self, nbLine: int, nbColumn: int, dist: float):
        self.drawLine(nbLine, nbColumn, dist)
        self.drawColumn(nbLine, nbColumn, dist)
        turtle.done()

    def drawLine(self, nbLine: int, nbColumn: int, dist: float):
        pass

    def drawColumn(self, nbLine: int, nbColumn: int, dist: float):
        pass

    def drawEdge(self, nbLine: int, nbColumn: int, dist: float):
        pass

    def setOriginPosition(self):
        turtle.setposition(-WIDTH//2, HEIGHT//2)

    # TODO écris moi la fonction dessin de la partie 2 :p


if __name__ == "__main__":
    GUI().drawGraph()
