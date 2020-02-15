# Official Name: Doung Lan Cheung
# Nickname: DC
# email: dcheun01@syr.edu
# Assignment: Assignment 3, problem 3
# Date: February 14, 2019
#make a graph, plot points with user input
from graphics import *
def main():
#create graphics window    
    win = GraphWin("Plot Points",700,600)
    win.setCoords(-4,-3,3,3)
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
#add an entry box for the number of points
    np = Text(Point(-3.5,2.6),"Number of Points")
    np.setSize(9)
    np.draw(win)
    pointBox=Entry(Point(-3.5, 2.4), 5)
    pointBox.setText(0)
    pointBox.draw(win)
#program reads the value user put in    
    win.getMouse()
    ptstr= pointBox.getText()
    pt = int(ptstr)
    
    x = Text(Point(-3.5,1.8),"x")
    x.draw(win)
    xBox=Entry(Point(-3.5,1.5),5)
    xBox.setText(0)
    xBox.draw(win)
    
    y = Text(Point(-3.5,0.7),"y")
    y.draw(win)
    yBox=Entry(Point(-3.5,0.5),5)
    yBox.setText(0)
    yBox.draw(win)
#print the (x,y) cooridinate on the graph    
    win.getMouse()
    for i in range(pt):
        xpt=float(xBox.getText())
        ypt=float(yBox.getText())
        label= Text(Point(xpt,ypt), i+1)
        label.setFill("red")
        label.draw(win)
        win.getMouse()
    win.Close()
main()