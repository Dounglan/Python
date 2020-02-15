# Official Name: Doung Lan Cheung
# Nickname: DC
# email: dcheun01@syr.edu
# Assignment: Assignment 3, problem 2
# Date: February 14, 2019
#Construct a graph with the horizontal lines being black and vertical: blue and labels, 0, 2, -2 in x and y directions. 
from graphics import *
def main():
    win =GraphWin("QuadRuled",600,600)
    win.setCoords(-3,-3,3,3)
#draw horizontal and vertical lines
    for v in range(12):
        x = 0.5*v
        VL = Line(Point(-3,-3),Point(-3,3))
        VL.move(x,0)
        VL.setFill("blue")
        VL.draw(win)
    for h in range(12):
        y = 0.5*h
        HL = Line(Point(-3,-3),Point(3,-3))
        HL.move(0,y)
        HL.setFill("black")
        HL.draw(win)
#add labels:center 0, -2, 2 in x-dir. -2,2 in y-dir
    origin = Text(Point(0,0), "0")
    origin.draw(win)
    xn2= Text(Point(-1.9,-.1),"-2")
    xn2.draw(win)
    x2 = Text(Point(2.1,-.1),"2")
    x2.draw(win)
    y2 = Text(Point(.1,2.1),"2")
    y2.draw(win)
    yn2=Text(Point(.1,-2.1),"-2")
    yn2.draw(win)
main()