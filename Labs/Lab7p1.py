#lab7p1
#Doung Lan Cheung. 
#Set up a window using user defined coordinates
#Draw Oval, explore copying an Oval using = (assignment)
#  versus using .clone()

from graphics import *

def main():
    #Set up the graphic window
    win=GraphWin("Lab 7",400,600)
    win.setBackground("lightyellow")
    
    #I want the height 4 units tall.
    #To keep proportions right, the width
    #should be 4/6*4 units, =8/3
    #LOWER left corner will still be 0,0
    #the right edge is 8/3, the top edge is 4
    rightEdge=8/3
    win.setCoords(0,0,8/3,4)
    
    #draw horizontal line 3/4 of the way down
    hl=Line(Point(0,1),Point(rightEdge,1))
    hl.setWidth(3)
    hl.draw(win)
    
    #Draw some shapes
    #draw the bounding box of an oval
    rect=Rectangle(Point(.2,3.5),Point(.4,2.5))
    rect.draw(win)
    #draw the oval
    ov=Oval(Point(.2,3.5),Point(.4,2.5))
    ov.setFill("darkBlue")
    ov.draw(win)
    
    #place some text
    Text(Point(rightEdge/2,.8),"Instructions").draw(win)
    midy=rightEdge/2
    
    #Give first instructions
    nextInstructions=Text(Point(midy,.6),"Click mouse to move oval.")
    nextInstructions.draw(win)
     
    #Move the oval.
    #Use a mouse click to start it, not using mouse location.
    win.getMouse()
    ov.move(.5,-1)
    
    #Change instructions
    nextInstructions.setText("Click mouse to move COPY of oval.")
    
    #Copy the oval.
    #Use a mouse click to start it, not using mouse location.
    win.getMouse()
    ovCopy=ov
    ovCopy.move(.5,1)
    
    #Change instructions
    nextInstructions.setText("Click mouse to move CLONE of oval.")
    
    #Clone the oval.
    #Use a mouse click to start it, not using mouse location.
    win.getMouse()
    ovClone=ov.clone()
    ovClone.move(.5,-1)
    ovClone.draw(win)
    #End of main()
main()    
    
    