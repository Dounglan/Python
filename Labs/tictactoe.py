#TicTacToe
#Illustrate building a list of moves and searching it
#to see if a square is occupied
#Using parallel lists to keep track of what color is there
#prints list data neatly in columns
#Dounglan Cheung
from graphics import *
import math
def setUpWindow():
    win=GraphWin("Tic Tac Toe", 600,600)
    win.setCoords(-1,-1, 4,4) #3x3 with 1 unit surrounding
    return win

#draw the grid
def makeGrid(win):
    #draw vertical lines
    for col in [1,2]:
        #Fill in values (take advantage of the loop values of col)
        aLine=Line(Point(col,0),Point(col,3))
        aLine.draw(win)
    #draw the horizontal lines    
    for row in [1,2]:
        #Fill in values (take advantage of the loop values of row)
        aLine=Line(Point(0,row),Point(3,row))
        aLine.draw(win)
    labelGrid(win)    
 
def labelGrid(win):
    for row in [0.5, 1.5, 2.5]:
        labelNum=str(4-math.ceil(row ) )
        #Fill in values for the Point coordinates
        label=Text(Point(-.5,row),labelNum)
        label.setSize(20)
        label.draw(win)
    for col in [0.5, 1.5, 2.5]:
        labelNum=str(math.ceil(col ) )
        #Fill in values for the Point coordinates
        label=Text(Point(col,3.5),labelNum)
        label.setSize(20)
        label.draw(win)
        
def drawEntryBoxes(win):
    #Fill in values for Points from your diagram
    rowBox=Entry(Point(0.6,-0.5),2)
    rowBox.setSize(30)
    rowBoxLabel=Text(Point(0,-0.5),"Row")
    rowBoxLabel.setSize(30)
    colBox=Entry(Point(1.8,-0.5),2)
    colBox.setSize(30)
    colBoxLabel=Text(Point(1.2,-0.5),"Col")
    colBoxLabel.setSize(30)
    rowBox.draw(win)
    rowBoxLabel.draw(win)
    colBox.draw(win)
    colBoxLabel.draw(win)
    clearBoxes(colBox,rowBox,win)
    return rowBox, colBox
    
# read the values in the entry boxes    
def readChoice(win, rowBox, colBox):
    win.getMouse()
    row = int(rowBox.getText())
    col = int(colBox.getText())
    return row, col

#checks to see if the spot is on the board and is not yet occupied
#returns true for a valid move
def checkValid( row, col, moveListPairs):
#onBoard should be true when row and col are values from 1 to 3
    
    st="("+str(col)+","+str(row)+")" #make the string (col,row)
#occupied should be true if the spot row, col is already occupied.
#test it by seeing if st in moveListPairs
    
#valid should be true only for valid moves (using onBoard and occupied)
    return valid  #true only for valid move

#print all the moves and who made them neatly at the top of screen 
def makeReport(moveListPairs,playerList,win):
    reportList=[] #this will be a list of items drawn in neat columns
    x=0
    item=0
    reportList.append(Text(Point(x,3.9),"good moves:"))
    reportList[item].setFace("courier")
    reportList[item].draw(win)
    x = .2
    for move in moveListPairs:
        item+=1
        x+=.5
        reportList.append(Text(Point(x,3.9),move))
        reportList[item].setFace("courier")
        reportList[item].draw(win)
    makePlayerReport(playerList,win)    
 
#print which players made which move in the list of moves. 
def makePlayerReport(playerList,win):
    x = 0.2
    p = Text(Point(x,3.7),"player:")
    p.setFace("courier")
    p.draw(win)
    for color in playerList:
        x += 0.5
        cL = Text(Point(x, 3.7), color)
        cL.setFace("courier")
        cL.draw(win)
#very similar to makeReport, but using playerList.
#Should be drawn underneath, but lined up with the list of moves.

def clearBoxes(colBox,rowBox,win):
       colBox.setText("0")
       rowBox.setText("0")
  
def main():
    win=setUpWindow()
    makeGrid(win)
    rowBox, colBox =drawEntryBoxes(win)
    moveList=[] #list of the valid moves, as Points
    moveListPairs=[] #list of strings of ordered pairs
    playerList=[] #list of who made corresponding move
    turn = 1
    while (len(moveList)<9):  #  3 turns.  Can change this
        row, col =readChoice(win, rowBox, colBox)
##        while not checkValid(row,col, moveListPairs):
##            clearBoxes(colBox,rowBox,win)
##            row, col =readChoice(win, rowBox, colBox)
        
#append a string that looks like "(col,row)" (with values)
#to moveListPairs
        moveListPairs.append("("+str(col)+","+str(row)+")")
        
#construct x,y - center of circle - corresponding to row and col
        x = col - 0.5
        y = (1*(3-row))+0.5
#append Point(x,y) to moveList.
        moveList.append(Point(x,y))
#construct circle centered at point
        circ = Circle(Point(x,y),0.25)
        if turn == 1:
#first turn color circle blue, and add blue to playerList
            circ.setFill("blue")
            playerList.append("blue")
            turn = 0
#second turn color circle red, and add red to playerList   
        elif turn == 0:    
            circ.setFill("red")
            playerList.append("red")
            turn = 1
#and so on for all moves
#draw the circle
        circ.draw(win)
        makeReport(moveListPairs,playerList,win)
#wait for mouse to close window
    win.getMouse()
    win.close()
##*************end of main*************** 
main() 