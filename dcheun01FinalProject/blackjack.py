#Dounglan Cheung
#Blackjack
#blackjack.py
#DUE May 1, 2019
#dcheun01

#*use ".sort" then do ".reverse" for sorting w/ decreasing for scores
#(IEB)read from an Entry box     done
#(OTXT)write to the screen using Text  done
#(IFL)read from an input file     done
#(OFL)write to an output file 
#(IMS)use the mouse's location    done
#(GW)open a GraphWin  done
#(FNC)call a function of your own design  done
#(RND)use a random number generator.  done
#(CLOD)define a class of your own design AND create an object of a class of your own design done
#(LOOD)use a list of objects of your own design    done

from graphics import *
from random import randrange

class Player:         #class for the input and output scores(player class)
    def __init__(self, name, win, lose, draw):
        self.name = name
        self.win  = win
        self.lose  = lose
        self.draw = draw
    def updateScore(self, s):
        if s == 1:
            win += 1
            return self.win
        elif s == 0:
            draw += 1
            return self.draw
        elif s == -1:
            lose += 1
            return self.lose
        
    def getName(self):
        return self.name
    def getWin(self):
        return self.win
    def getLose(self):
        return self.lose
    def getDraw(self):
        return self.draw
    def display(self,win,x,y):
        print("Player:{0:<20}Wins:{1:,} Loses:{2:,} Draws:{3:,}".format(self.name, self.win, self.lose, self.draw)) 
        Text(Point(x,y),"Player:{0:<20}Wins:{1:,} Loses:{2:,} Draws:{3:,}".format(self.name, self.win, self.lose, self.draw))

def useWin(aPlayer):    
    return aPlayer.getWin()

def useLose(aPlayer):    
    return aPlayer.getLose()

def useDraw(aPlayer):    
    return aPlayer.getDraw()

def useName(aPlayer):
    return aPlayer.getName()

def processString(line):    
    item = line.split("\t")
    name = item[0].strip()
    win = int(item[1].strip())
    lose = int(item[2].strip())
    draw = int(item[3].strip())
    s = Player(name, win, lose ,draw)
    return s        

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def drawCard(self,win,x,y): #helps draws card
        Text(Point(x,y), self.rank + self.suit).draw(win)    
    
    def getValue(self): #helps get Value(ex. 3-spade symbol as  a  card)
        return self.rank + self.suit
    
    def readValue(self):  #have read value in class or put outside of class?
        if self.rank == 'J' or self.rank == 'Q' or self.rank =='K' or self.rank == '10':
            return int(10)       #card[:1] example '2' out of the full '2 of Hearts' string
        elif self.rank == '2' or self.rank == '3' or self.rank == '4' or self.rank == '5' or self.rank == '6' or self.rank == '7' or self.rank == '8' or self.rank == '9':
            return int(self.rank)
        elif self.rank == 'A':   #if over 11, Ace = 1, else Ptotal or Dtotal <11 Ace = 11
            return int(11)
        
def checkButtonClick(clickedPoint, leftLower, rightUpper): #makes sure button is clicked only at the box
    if (clickedPoint.getX() >= leftLower.getX()) and (clickedPoint.getX() <= rightUpper.getX()) and (clickedPoint.getY() >= leftLower.getY()) and (clickedPoint.getY() <= rightUpper.getY()):
        return 1
    else:
        return 0

def introWindow():    #welcome screen
    win = GraphWin("Blackjack", 800, 600)
    win.setCoords(-10,-10,10,10)
    Text(Point(0,6),"Welcome to Blackjack!").draw(win)
    Text(Point(-1,4), "Player name").draw(win)
    playerBox=Entry(Point(2,4), 15)
    playerBox.setText("")
    playerBox.draw(win)
    start = Rectangle(Point(-2.5,-0.5), Point(3.3,1.5))
    start.setFill("grey")
    start.draw(win)
    buttonLabel=Text(Point(0,0),"Click here to start the game")
    buttonLabel.draw(win)
    intro1 = Text(Point(0,-2),"Blackjack(21) is a casino game played with cards.\nGoal:draw cards that total as close to 21 points, as possible without going over(whose hand>21 will is_bust).\nAll face cards count as 10 points. Aces count as 1 or 11, and all other cards count their numeric value.")
    intro1.draw(win)
    clickedPoint = win.getMouse()
    while checkButtonClick(clickedPoint, Point(-2.5,-0.5), Point(3.3,1.5)) != 1:
        clickedPoint = win.getMouse() 
        if checkButtonClick(clickedPoint, Point(-2.5,-0.5), Point(3.3,1.5)) == 1:
            name = playerBox.getText()
            player = Player(name,0,0,0)
            win.close()
            return player
    win.close()
    return None

def gameWindow():     #playing screen
    win = GraphWin("Blackjack", 800, 600)
    win.setCoords(-10,-10,10,10)
    hit = Rectangle(Point(5,.5), Point(6.5,1.5))          #hit/stand buttons
    hit.setFill("grey")
    hit.draw(win)
    hitButton=Text(Point(5.5,1.2),"Hit")
    hitButton.draw(win)    
    stand = Rectangle(Point(5,-.5), Point(6.5,.5))
    stand.setFill("grey")
    stand.draw(win)
    standButton=Text(Point(5.5,.15),"Stand")
    standButton.draw(win)
    for i in range(6):     #displays the empty card slots
        x = i*3
        pcardslot = Rectangle(Point(-9,-9), Point(-7.5,-5.5))
        pcardslot.move(x,0)
        pcardslot.draw(win)
    for i in range(6):
        x = i*3
        dcardslot = Rectangle(Point(-9,9), Point(-7.5,5.5))
        dcardslot.move(x,0)
        dcardslot.draw(win)
    return win

def cardDeck():      #make deck and shuffles deck
    rank = ['A','2','3','4','5','6','7','8','9','J','Q','K'] 
    suit = [u"\u2660",u"\u2663",u"\u2665",u"\u2666"]   #spade,club, heart, diamond
    deck = []    
    for i in suit:
        for j in rank:
            deck.append(Card(j,i))
    for k in range(len(deck)):
        r = randrange(k, len(deck))
        deck[k], deck[r] = deck[r], deck[k]        
    return deck

def getCard(deck):  #gets the card for the player and dealer from shuffled deck
    r = randrange(0, len(deck))
    temp = deck[r]
    del deck[r]  #prevents the 2 of the same cards in a deck
    print(temp.getValue())
    return temp

def initialPlay(win):
    deck = cardDeck()  #sets up shuffled deck
    card1 = getCard(deck) #player card    (self.rank+self.suit)
    card2 = getCard(deck) # player card
    card3 = getCard(deck) #dealer card
    card4 = getCard(deck) #dealer card    
    card1.drawCard(win,-8.2,-7.2)  #put x and y, now can do any future card
    card2.drawCard(win, -5.2, -7.2)
    card4.drawCard(win, -5.2, 7.2)
    playera = card1.readValue() #reading value w/ class
    playerb = card2.readValue()
    dealerc = card3.readValue()
    dealerd = card4.readValue() 
    Ptotal = playera + playerb     #player's initial points
    Dtotal = dealerc + dealerd     #dealers' initial points
    print("Player starts: " + str(Ptotal)+".", "Dealer starts: " +str(Dtotal)+".")
    return Ptotal, Dtotal, card1, card2, card3, card4

#def eval_ace(Ptotal, Dtotal,card1,card2,card3,card4):  #if have time(difficulty points possibly)
## Determine Ace = 1 or 11, relying on total hand.   
#    if Ptotal <= 11 or :
#        
#    
#    return Ptotal, Dtotal
## at position, where Ace == 11, replace by Ace == 1.
#    else:

def Game(win):    #gameplay
    Ptotal, Dtotal, card1,card2,card3,card4 = initialPlay(win)
    s = 0
    if Ptotal == 21:
        Text(Point(0,1),"Player total: "+ str(Ptotal)).draw(win)
        Text(Point(0,2),"Dealer total: "+ str(Dtotal)).draw(win)        
        Text(Point(0,0),"Blackjack, You win!")
#        s.updateScore(s)
        Continue(win)
    else:
        while Ptotal < 21:     #no win or lose yet
            ans = win.getMouse()
            if checkButtonClick(ans, Point(5,-.5), Point(6.5,0.5)) == 1: #user clicks stand, dealer gets cards
                if Dtotal <17:
                    deck = cardDeck()
                    card = getCard(deck)
                    card.drawCard(win,-2.2, 7.2)
                    card_value = card.readValue()
                    Dtotal += card_value
                    ans = win.getMouse()
                    if (Dtotal > 21 and Ptotal <= 21): # you win
                        card3.drawCard(win,-8.2, 7.2)
                        Text(Point(0,1),"Player total: "+ str(Ptotal)).draw(win)
                        Text(Point(0,2),"Dealer total: "+ str(Dtotal)).draw(win)
                        Text(Point(0,0),"You win! :)").draw(win)
                        Continue(win)
                        s += 1
                    elif (Dtotal <= 21 and Dtotal > Ptotal): #you lose
                        card3.drawCard(win,-8.2, 7.2)
                        Text(Point(0,1),"Player total: "+ str(Ptotal)).draw(win)
                        Text(Point(0,2),"Dealer total: "+ str(Dtotal)).draw(win)
                        Text(Point(0,0),"You lose! :(").draw(win)
                        Continue(win)
                        s-= 1
                    else:
                        continue
                elif Ptotal == Dtotal:
                    card3.drawCard(win,-8.2, 7.2)
                    Text(Point(0,1),"Player total: "+ str(Ptotal)).draw(win)
                    Text(Point(0,2),"Dealer total: "+ str(Dtotal)).draw(win)
                    Text(Point(0,0),"Draw").draw(win)
                    Continue(win)
                    s==0
                elif Dtotal < Ptotal or Dtotal > 21:
                    card3.drawCard(win,-8.2, 7.2)
                    Text(Point(0,1),"Player total: "+ str(Ptotal)).draw(win)
                    Text(Point(0,2),"Dealer total: "+ str(Dtotal)).draw(win)
                    Text(Point(0,0),"You win :)").draw(win)
                    Continue(win)
                    s+=1
                else:
                    card3.drawCard(win,-8.2, 7.2)
                    Text(Point(0,1),"Player total: "+ str(Ptotal)).draw(win)
                    Text(Point(0,2),"Dealer total: "+ str(Dtotal)).draw(win)
                    Text(Point(0,0),"You lose :(").draw(win)
                    Continue(win)
                    s-=1
                    continue
            elif checkButtonClick(ans, Point(5,.5), Point(6.5,1.5)) == 1:  #user clicks hit, user&dealer get cards
                deck = cardDeck()
                card = getCard(deck)
                card.drawCard(win, -2.2,-7.2)
                card_value = card.readValue()
                dcard = getCard(deck)
                dcard.drawCard(win, -2.2, 7.2)
                dcard_value = dcard.readValue()
                Dtotal += dcard_value
                Ptotal += card_value
                if Ptotal > 21: #lose condition
                    card3.drawCard(win,-8.2, 7.2)
                    Text(Point(0,0),"You LOSE!").draw(win)
                    Text(Point(0,1),"Player total: "+ str(Ptotal)).draw(win)
                    Text(Point(0,2),"Dealer total: "+ str(Dtotal)).draw(win)
                    Continue(win)
                    s-=1
                elif Ptotal == 21: #winning condition
                    card3.drawCard(win,-8.2, 7.2)
                    Text(Point(0,0),"You win!").draw(win)
                    Text(Point(0,1),"Player total: "+ str(Ptotal)).draw(win)
                    Text(Point(0,2),"Dealer total: "+ str(Dtotal)).draw(win)
                    Continue(win)
                    s+=1
                elif Ptotal == Dtotal:
                    card3.drawCard(win,-8.2, 7.2)
                    Text(Point(0,1),"Player total: "+ str(Ptotal)).draw(win)
                    Text(Point(0,2),"Dealer total: "+ str(Dtotal)).draw(win)
                    Text(Point(0,0),"Draw").draw(win)
                    Continue(win)
                    s==0
                else:
                    continue

def trackScore(): #keeps track of score
    win2 = GraphWin("Scores", 300, 300)
    win2.setCoords(-10,-10,10,10)
    infile = open("blackjackRecords.txt","r")  #input
    aList = []
    content = infile.readline()
    for line in infile:
        st = processString(line)
        st.display(win2,0,9)
        aList.append(st)
    outfile = open("blackjackData.txt","w")
    a = outfile.append(player, infile=outfile)
    Player(player, win,lose,draw)
    
    infile.close()
    win2.getMouse()
    win2.close()

def Continue(win):   #want to play again? window option 
    win1 = GraphWin("Continue?", 200, 150)
    win1.setCoords(-10,-10,10,10)
    Text(Point(0,7),"Do you want to play again?").draw(win1)
    Text(Point(-4,0), "Yes").draw(win1)
    Text(Point(4,0), "No").draw(win1)
    yesButton = Rectangle(Point(-5,-3),Point(-3,-1))
    yesButton.setFill("green")
    noButton = Rectangle(Point(3,-3),Point(5,-1))
    noButton.setFill("red")
    yesButton.draw(win1)
    noButton.draw(win1)
    clickedPoint = win1.getMouse()    
    while checkButtonClick(clickedPoint, Point(3,-3),Point(5,-1)) != 1:    #if the user hits no, closes the game
        if checkButtonClick(clickedPoint, Point(-5,-3),Point(-3,-1)) == 1: #if yes was clicked, makes a new game
            win1.close()
            win.close()
            main()
        clickedPoint = win1.getMouse()
    win1.close()
    win.close()
    return None


def main():
    introWindow() #opens starting screen
    
    win = gameWindow()  #opens game window, sets up game
    Game(win) #gameplay
    
    track()
    win.close()
main()