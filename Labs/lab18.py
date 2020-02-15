#Dounglan Cheung
#lab18
#partI
from graphics import *
import time
from random import randrange
class BBall:
    def __init__(self, color, center, dir=1):
        self.circle = Circle(center,1)
        self.color = color
        self.direction = dir
        
    def draw(self,win):
        self.color = self.circle.setFill(self.color)
        self.circle = self.circle.draw(win)
        
    def move(self,win):
        y = self.circle.getCenter().getY()
        if y == -8:
            self.direction = 1
        elif y == 8:
            self.direction = -1
        self.circle.move(0, self.direction)   
#part IV B       
    def changeColor(self):
        colors =["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white", "grey"]
        total = len(colors)
        random = randrange(0,total)
        color = colors[random]
        self.circle.setFill(color)
        
def main():
    win = GraphWin("BBall",600,600)
    win.setBackground("black")
    win.setCoords(-8,-8,8,8)
    c = Point(0,-8)
    Ball = BBall("red", c)
    Ball.draw(win)
    Ball.move(win)
    
    d = Point(5,8)
    downBall = BBall("blue", d)
    downBall.draw(win)    
    downBall.move(win)
    downBall.move(win)
    
    e = Point(-3,0)
    midUp = BBall("green",e) 
    midUp.draw(win)
    midUp.move(win)
    midUp.move(win)
    midUp.move(win)
    
    f = Point(-6,0)
    midDown = BBall("purple",f,dir=-1)
    midDown.draw(win)
    midDown.move(win)
    midDown.move(win)
    midDown.move(win)
     
#    while True:
#        downBall.move(win)
#        midUp.move(win)
#        midDown.move(win)
#        Ball.move(win)
#        time.sleep(.03) 
    
    while win.checkKey() != 'q':
        Ball.move(win)
        if win.checkMouse() != None:
            Ball.changeColor()
            downBall.changeColor()
            midUp.changeColor()
            midDown.changeColor()
        downBall.move(win)
        midUp.move(win)
        midDown.move(win)
        Ball.move(win)
        time.sleep(.02)
    
    win.close()
main()