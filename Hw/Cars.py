#Doung Lan Cheung
#dcheun01@syr.edu
#Assignment 6, problem c
#Draw a car, 
from graphics import *
#set ups graphics window, returns the window
def setUpWindow():
    win = GraphWin("Cars",600,600)
    win.setCoords(0,0,6,6)
    return win
#draws car, gets an anchor point, returns car
def drawCar(p, win):
#draw car body    
    goodX = p.getX()
    goodY = p.getY()
    rect = Rectangle(p, Point(goodX + 1.6,goodY - 0.5)) 
    rect.setFill("green")
    rect.draw(win)
#draw wheels    
    circ = Circle(Point(goodX + 0.3, goodY - 0.7), 0.22)
    circ1 = Circle(Point(goodX + 1.3, goodY - 0.7), 0.22)
    circ.setFill("black")
    circ1.setFill("black")
    circ.draw(win)
    circ1.draw(win)
    return rect, circ, circ1
#creates the car and uses the clicks on the graphics window to print the car location
def main():
    win = setUpWindow()
    win.setBackground("light blue")
    p = win.getMouse()
    drawCar(p, win)
    for i in range(4):
        p =win.getMouse()
        drawCar(p, win)
    win.getMouse()    
    win.close()
main()