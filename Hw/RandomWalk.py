#Dounglan Cheung
#dccheun01@syr.edu
#Assignment 8, problem 1
#April 4,2019
#simulate walking with a grid and circles
from graphics import *
from random import randrange
#set up window
def setupWindow():
    win = GraphWin("RandomWalk", 600, 600)
    win.setCoords(-5,-5,5,5)
    return win
#draw horizontal and vertical lines
def linepaper(win):
    for v in range(12):
        x = 1*v
        VL = Line(Point(-5,-5),Point(-5,5))
        VL.move(x,0)
        VL.setFill("blue")
        VL.draw(win)
    for h in range(12):
        y = 1*h
        HL = Line(Point(-5,-5),Point(5,-5))
        HL.move(0,y)
        HL.setFill("black")
        HL.draw(win)
#add labels:center 0, -5, 5 in x-dir. -5,5 in y-dir.
    origin = Text(Point(0,0), "0")
    origin.draw(win)
    xn2= Text(Point(-4.9,-.1),"-5")
    xn2.draw(win)
    x2 = Text(Point(4.9,-.1),"5")
    x2.draw(win)
    y2 = Text(Point(0.1,4.9),"5")
    y2.draw(win)
    yn2=Text(Point(0.1,-4.9),"-5")
    yn2.draw(win)
#create circles simulating walking by one unit in vertical and horizontl direction 
def walk(win):
    start = Circle(Point(0,0),0.25)
    start.setFill("green")
    start.draw(win)
    x = 0
    y = 0
    count = 0
    while x > -4 and x < 4 and y < 4 and y > -4:
        count = count + 1
        a = randrange(0,4)
        if a==0:
            x = x + 1
        elif a==1:
            x= x - 1
        elif a==2:
            y = y + 1
        elif a==3:
            y = y - 1
        step = Circle(Point(x,y),0.25)
        step.setFill("red")
        step.draw(win)
#print the steps until they go out of bounds
    Text(Point(0,4.0),"Count =").draw(win)
    Text(Point(.5, 4.0), count).draw(win)
    
def main():
    win = setupWindow()
    linepaper(win)
    walk(win)
main()