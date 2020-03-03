#Dounglan Cheung
#CIS 400 assignment 1
#February 7,2020

#at least 100 code lines 
#list comprehension  done
#loops(for or while) done
#input               done 
#if-elif             done
#define a class      done
#dictionary comp     done
#try-Exception       done

from random import randrange

class Country:  #creates a class for country
    def __init__(self, name, population):
        self.name = name 
        self.population = population

    def display(self):
        print("{0:<20}Population:{1:,}".format(self.name, self.population)) #prints the display
        
    def getPopulation(self):
        return self.population #grabs population

    def getName(self): #grabs the name of the country
        return self.name
    
def makeACountry(line):    
    item = line.split("\t") 
    name = item[0].strip() #strips everything after the first index which is a country name
    pop = int(item[1].strip().replace(",","")) #strips, replaces the commas and turns the string of population number into an int
    c = Country(name, pop) #uses the Country class while grabbing the country's name and its population
    return c

def usePopulation(aCountry):    
    return aCountry.getPopulation()
    
def useName(aCountry):
    return aCountry.getName()

def orderCountry():
    countryList = []
    infile = open("countries.txt","r") #opens file
    for line in infile: #reads each line in the txt file and displays each line in the shell
        country = makeACountry(line) 
        country.display()   #displays the input from the txt file

        countryList.append(country)
    print("*"*50) #splits the original txt file output from the sorted list
    
    question = input("Would you like to sort the list by name or by population? (Enter 'n' for name or 'p' for population.) ")
    while not(question == "n" or  question == "N" or question == "P" or question == "p"):
        question = input("Would you like to sort the list by name or by population? (Enter 'n' for name or 'p' for population.) ")        
#depending on user choice, it will sort wither by name or population and if anything else is entered it will, ask again
    if ((question == 'n') or (question == 'N')):
        countryList.sort(key=useName)
        for i in countryList: #displays the countries alphabetically
            i.display()
    
    elif ((question == 'p') or (question == 'P')):
        countryList.sort(key=usePopulation)
        for i in countryList: #displays the countries from lowest number to highest number
            i.display()
    
    infile.close() #closes the file
    

def steps():
    ask = input("Do you want to see all the steps for the shuffled deck?(y/n) ")
    while not(ask == "y" or  ask == "n" or ask == "Y" or ask == "N"): #asks the user for y or n input, if any other character is entered then it will keep asking
        ask = input("Do you want to see all the steps for the shuffled deck?(y/n) ")        
        return ask
    return ask

def makeDeck():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] #deck of cards
    return deck

def Shuffle(deck, show): #shuffles the deck
    num = len(deck)  #takes length of the deck 
    for i in range(num): #reads and swaps the random index of the list of cards from the original index from the cards
        random = randrange(i, num)
        deck[i], deck[random] = deck[random], deck[i]
        if show == True: #this will show each step with shuffling the deck
            print(deck)
    return deck

def continue_shuffle():
    q = input("Would you like to shuffle again? (y/n) ") #asks to continue shuffling the deck
    if (q == "Y" or q == "y"):
        print("Let's start from beginning.")
        cardShuffler() #will call the function again thus asking if user would like to shuffle again
    elif (q == "N" or q == "n"):
        print("Okay, shuffling program is done\n")
    else:
        continue_shuffle() #if anything else is entered other than n,y,N,Y , then it will cll the function again

def cardShuffler():
    deck = makeDeck() #sets variable deck and calls makeDeck() which returns a list of a deck
    print("Starting deck: ", deck)
    ask = steps() 
    if (ask == "y" or ask == "Y"):
        shuffle = Shuffle(deck,True)
    else:
        shuffle = Shuffle(deck,False)
    print("Shuffled deck: " , shuffle)
    continue_shuffle()
    
    
def roll(): #randomizes the number from 1 to 6
    r = randrange(1,7) 
    return r

def diceCounter(): #creates a dice counter where it is the sum of two dice and how counts the frequecy of that number
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numRolls = int(input("How many times do you want to roll the two dice together? ")) #asks how many times you want to roll the two dice
    for i in range(numRolls): #takes the number of rolls and loops it from 0 to the number of rolls
        red = roll() #dice 1
        green = roll() #dice 2
        r = red + green #the 2 dice together
        counter[r] = counter[r] + 1
    count = 0
    print("Sum of dice \tFrequency")
    for value in counter:
        print(count,"\t\t", value)
        count = count + 1
        

def dictionary(): #creates a dictionary called deserts, prints the name from each index of the list and along with the length of the name
    desserts = ['pie', 'candy', 'cake', 'chocolate', 'cookie']
    for name in desserts:
        print(name ,":" , len(name)) 
    greetings = ['hi', 'hello', 'good morning', 'good afternoon', 'salutations', 'hey']
    print( {word : len(word) for word in greetings} ) #concatenates the word in each index of greetings with the length of each word in the respected index
        
def try_except(): #it will ask the user for two numbers and it will try to divide the two numbers by each other and print the solution, and if not, it will print the zerodivision error.
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    try:
       solution = a / b
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print("The answer is ", solution)
    finally:
        print("Goodbye!") #prints this to make sure that it is the end of the function
    
    
def main(): #calls the functions and the program will only run in what is in main
    cardShuffler() 
    diceCounter() 
    dictionary() 
    try_except() 
    orderCountry() 
main() 