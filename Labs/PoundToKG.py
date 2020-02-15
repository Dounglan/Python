#PoundToKG.py
#Baruch
#Interactive graphics program that converts
#  pounds to kilograms
from graphics import *
def main():
    #Set up the graphic window
    win=GraphWin("Pounds Kilograms Converter",400,600)
    win.setBackground("yellow2")
#I want the height 6 units tall.
#To keep proportions right, the width
#should be 4
#LOWER left corner will be 0,0
    win.setCoords(0,0,4,6)
#draw horizontal line 
    hl=Line(Point(0,2),Point(4,2))
    hl.setWidth(3)  # set thickness of line
    hl.draw(win)
#make a fake button for clicking for computation
    button=Rectangle(Point(1,1.5),Point(3,.5))
    button.setFill("lightgray")
    buttonLabel=Text(Point(2,1),"Click to Calculate")
    button.draw(win)
    buttonLabel.draw(win) 
#draw text entry box for entering weight in pounds
    Text(Point(1.3,5.7),"Weight in pounds").draw(win)
    poundBox=Entry(Point(1, 5.5), 10)
    poundBox.setText("0.0")  #default value will be 0.0
    poundBox.draw(win)
#display weight in kilograms.
    Text(Point(3.3,5.7),"Weight in Kg").draw(win)
    kg=0  #default value
    KGdisplay=Text(Point(3, 5.5),str(kg))
    KGdisplay.draw(win)
#read value in entry box, compute and display kilograms
    win.getMouse()
    pounds=float(poundBox.getText())
    kg=pounds*0.453592
    KGdisplay.setText(str(kg))
main()       