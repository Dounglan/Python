#Doung Lan Cheung
#Lab7p2.py
from graphics import *

def main():
#Set up graphics window    
    win=GraphWin("Lab7p2",300,400)
#set cooridinates    
    win.setCoords(0,0,3,4)
#draw pink circle    
    c = Circle(Point(.5,3.5),.3)
    c.setFill("pink")
    c.draw(win)
#click mouse 5 times to move circle to the right
#    midy=4/2
    Text(Point(1.5,2),"Instructions").draw(win)
    nextInstructions=Text(Point(1.5,1),"Click mouse 5 times.")
    nextInstructions.draw(win)
    for q in range(5):
        win.getMouse()
        c.move(.19,-0.05)
#click mouse to close graphics window
    nextInstructions.setText("Click mouse to close window.")
    win.getMouse()
    win.close()
#draw a blue rectangle and clone it with green color
    r = Rectangle(Point(0.5,1), Point(0.7,1.5))
    r.setFill("blue")
    r.setOutline("light blue")
    r.draw(win)
#Clone rectangle
    rClone=r.clone()
    rClone.move(.5,0)
    rClone.setFill("green")
    rClone.setOutline("dark green")
    rClone.setWidth(5)
    rClone.draw(win)
#draw vertical line halfway between rectangles
    L = Line(Point(.85,0), Point(.85,4))
    L.setFill("magenta")
    L.draw(win)
main()