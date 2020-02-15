#Dounglan Cheung
#dccheun01@syr.edu
#Assignment 7, problem 2
#March 28,2019
#Create 3 colored rectangles then with a click on one of them it fills in an empty circle with chosen color, and if blank rectangle is clicked, then it closes the program
from graphics import *
#set up window
def setupWindow():
    win = GraphWin("Color Chooser", 600, 600)
    win.setCoords(0,0,6,6)
    return win
#make clicking the button valid or invalid
def checkButtonClick(clickedPoint, leftLower, rightUpper):
    if (clickedPoint.getX() >= leftLower.getX()) and (clickedPoint.getX() <= rightUpper.getX()) and (clickedPoint.getY() >= leftLower.getY()) and (clickedPoint.getY() <= rightUpper.getY()):
        return 1
    else:
        return 0
    
def main():
    win = setupWindow()
#draws 1st rect
    rect1 = Rectangle(Point(.7,4), Point(1.5,4.5))
    rect1.setFill("black")               
    rect1.draw(win)
#draw 2nd rect
    rect2 = Rectangle(Point(2.7,4), Point(3.5,4.5))
    rect2.setFill("red")
    rect2.draw(win)
#draw 3rd rect    
    rect3 = Rectangle(Point(4.6,4), Point(5.4,4.5))
    rect3.setFill("blue")
    rect3.draw(win)
#draw the rect that closes program    
    rQuit = Rectangle(Point(2.5,1.5), Point(3.3,2))
    rQuit.draw(win)
    buttonLabel=Text(Point(2.75,1.75),"Quit")
    buttonLabel.draw(win)
    Text(Point(2.6,.8),"Instructions: Click the rectangles and to close the program: click quit").draw(win)
#draw empty circle     
    circ = Circle(Point(3,5.5), .40)
    circ.draw(win)
#create a sentinel/data verfication loop using the mouse that changes circle's color    
    clickedPoint = win.getMouse()
    while checkButtonClick(clickedPoint, Point(2.5,1.5), Point(3.3,2)) != 1:                 
        if checkButtonClick(clickedPoint, Point(.7,4), Point(1.5,4.5)) == 1:
            circ.setFill("black")
        elif checkButtonClick(clickedPoint, Point(3,4), Point(3.8,4.5)) == 1:
            circ.setFill("red")
        elif checkButtonClick(clickedPoint, Point(5,4), Point(5.8,4.5)) == 1:
            circ.setFill("blue")
        clickedPoint = win.getMouse() 
    win.close()
main()