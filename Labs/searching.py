#Dounglan Cheung
#searching.py
def binarySearch(list, key):
    lowIndex = 0
    highIndex = len(list) -1 
    found = False
    
    while (lowIndex >= highIndex) or found == False:
        midIndex = (highIndex + lowIndex)//2
        if list[midIndex] == key:
            found = True
        elif list[midIndex] > key:
            highIndex = midIndex - 1
        else:
            lowIndex = midIndex + 1
    if found:
        return midIndex   
    else:
        return -1
    
def main():
    list = []
    for i in range(10):
        list.append(i)
    print(list)
    key = 5
    a = binarySearch(list, key)
    print(a)
    
    
    infile = open("bigList.txt","r")
    aList = infile.readlines()
    for line in aList:
        aList = line.split()
    
    for i in range(len(aList)):
        aList[i] = int(aList[i])
    print(aList)
    
    key = 1017
    b = binarySearch(aList, key)
    print(b)
    
main()