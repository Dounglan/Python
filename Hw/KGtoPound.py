#Doung Lan Cheung
#KGtoPound.py
#kilograms to pounds
from graphics import *
def main():
    win=GraphWin("Kilograms to Pounds Converter",400,600)
    win.setBackground("light blue")
    win.setCoords(0,0,4,6)
#make fake button for conversion
    button=Rectangle(Point(1,1.5),Point(3,.5))
    button.setFill("grey")
    buttonLabel=Text(Point(2,1),"Click to Calculate")
    button.draw(win)
    buttonLabel.draw(win)
#draw weight in kilograms   
    Text(Point(1,5.7),"Weight in pounds").draw(win)
    lbs = 0
    lbdisplay=Text(Point(1,5.5),str(lbs))
    lbdisplay.draw(win)
#display text entry box for entering weight in kilograms    
    Text(Point(3.3,5.7),"Weight in Kg").draw(win)
    KgBox=Entry(Point(3,5.5),10)
    KgBox.setText("0.0")
    KgBox.draw(win)
#calculate kilograms to pounds
    win.getMouse()
    kg=float(KgBox.getText())
    pounds= kg/0.453592
    lbdisplay.setText(str(pounds))
main()