# Official Name: Doung Lan Cheung
# Nickname: DC
# email: dcheun01@syr.edu
# Assignment: Assignment 3, problem 1:Candy.py
# Date: February 14, 2019
#Draw an oval table with 10 candry bars on it
from graphics import *
def main():
#make window    
    win=GraphWin("Sweet Engineering",400,600)
    win.setBackground("red3")
    win.setCoords(0,0,4,4)
#get title
    Text(Point(1.8,3.6),"Sweet Engineering").draw(win)
#get oval shape table
    o = Oval(Point(.5,.7),Point(3,3.5))
    o.setFill("tan")
    o.draw(win)
#get 10 candy bars    
    for i in range(10):
        y = .1+i*.2
        r =Rectangle(Point(1.5,3.2),Point(2,3.3))
        r.setFill("green")
        r.move(0,0.01-y)
        r.draw(win)
main()