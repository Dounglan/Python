#lab6Text
#Doung Lan Cheung
#Set up a window using user defined coordinates
#Make a line across, 3/4 of the way down.
#Under this line will go instructions for user interaction
#Above it will be the picture.
from graphics import *
def main():
#Set up the graphics window
    win=GraphWin("Lab 6",600,800)
    win.setBackground("lightyellow")
#I want the height 4 units tall.
#To keep proportions right, the width
#should be (600/800)*4 = 3 units
#LOWER left corner will be 0,0
    rightEdge=3
    topEdge=4
    win.setCoords(0,0,rightEdge,topEdge)
#draw horizontal line 3/4 of the way down
    hl=Line(Point(0,1),Point(rightEdge,1))
    hl.setWidth(3)
    hl.draw(win)
#Set up instructions
    midy=rightEdge/2
    Text(Point(midy,.8),"Instructions").draw(win)
    nextInstructions=Text(Point(midy,.6),"Click mouse 5 times.")
    nextInstructions.draw(win)
#get mouseclick, draw circle there.  Repeat 5 times.
    for i in range(5):
        p=win.getMouse()
        c=Circle(p,0.1)
        c.setFill("red1")
        c.draw(win)
#Change instructions
    nextInstructions.setText("Click mouse AND press a letter.\nThree times total.")
#get mouseclick, get a keyboard key, draw the letter there.  Repeat 3 times.
    for i in range(3):
        p=win.getMouse()
        k=win.getKey()
        klabel=Text(p,k+k)
        klabel.draw(win)
#click mouse to close window
    nextInstructions.setText("Click mouse to close window.")
    win.getMouse()
    win.close()  
#End of main()
main()