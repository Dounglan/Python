#DounglanCheung
#SimplisticCardDealer.py
#Simulate dealing a hand of cards.  (May have repeats)
#import library so we can use randrange
from random import randrange
#Return a random rank for a card, that is
#returns a random character from "A23456789TJQK"
#Notice the use of T for ten
def chooseRank():
    ranks="A23456789TJQK"
    max = randrange(13)
    rank = ranks[max]
    return rank
#Return a random suit for a card, that is
#return a random character from "CDHS"
def chooseSuit():
    suits="CDHS"
    s = randrange(4)
    symb = suits[s]
    return symb
#Create a hand of 7 cards.
def main():
    #initialize hand as an empty list
    hand = []
    # repeat 7 times, once for each card
    for i in range(7):
        #pick a random rank and suit
        rank = chooseRank()
        suit = chooseSuit()
        #append a string with that rank and suit 
        #to the list hand
        hand.append(rank+suit)
    #print the hand
    print(hand)
    #sort the hand and print it again
    hand.sort()
    print(hand)
main()