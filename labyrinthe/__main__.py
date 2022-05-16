#!/usr/bin/env python
# -*- coding: utf-8 -*-

import labyrinthe.GUI as G
import labyrinthe.Labyrinthe as L
import turtle
import time
turtle.hideturtle()
main = G.GUI()
time.sleep(5)
labyrinthe = L.Labyrinthe
main.showLabyrinthe(labyrinthe, 4, 8)
main.showGraph(labyrinthe, 4, 8)
main.drawParcours(labyrinthe)
main.showChemin(labyrinthe)
turtle.done()
