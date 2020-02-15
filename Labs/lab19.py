#Dounglan cheung
#lab19
import math
from random import randrange 
# read numbers from a file into a list
# numbers are ints
# fileName is the name of the file
# returns the list
#part II A
def readNumbers(fileName):
    numfile = open(fileName,"r")
    numList = []
    for line in numfile:
        numList.append(int(line))
    numfile.close()
    print(numList)
    return numList
#PArt II B
def average(aList):
    count = 0
    tot = 0
    for num in aList:
        tot = tot + num
        count = count + 1
    average = tot/count
    return average
#part II C
def stdDev(aList, avg):
    std = 0
    for i in aList:
        std += (avg-i)**2
    standev = math.sqrt(std/len(aList))
    return standev
#part II D
def copy(aList):
    copyList = []
    for i in aList:
        copyList.append(i)
    aList[2] = 56
    print(aList)
    print(copyList)
    return copyList

#part II E
def median(aList):
    aList.sort()
    if len(aList)%2 == 1:
        median = aList[(len(aList)-1)//2]
        return median
    elif len(aList)%2 == 0:
        median1 = (len(aList/2))
        median2 = (len(aList)/2)-1
        return median1, median2
#Part III A
def makeList(n):
    myList = []
    for i in range(n):
        myList.append(i+1)
    print(myList)
    return myList
#Part III B/C
def shuffle(myList):
    for i in range(len(myList)):
        r = randrange(i, len(myList))
        myList[i], myList[r] = myList[r], myList[i]
    print("Shuffled List: ",myList)
    return myList

def main():
    fileName = "ages.txt"
    numList = readNumbers(fileName)
    aList = numList
    avg = average(aList)
    print("Average is ", avg)
    standev = stdDev(aList, avg)
    print("Standard Deviation is ", standev)
    copy(aList)
    mid = median(aList)
    print("Median is ", mid)
    n = 10
    myList = makeList(n)
    shuffleList = shuffle(myList)
main()