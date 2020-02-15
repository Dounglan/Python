#Dounglan Cheung
#dccheun01@syr.edu
#Assignment 7, problem 1
#March 28,2019
#draw shapes with stars 
#set up function to draw rectangle
def drawRect(width,height,pictureFile):
    for i in range(height):
        for a in range(width):
            print("*",end="", file=pictureFile)
        print(file=pictureFile)
    return height, width
#set up function to draw square w/ rectangle function
def drawSquare(side,pictureFile):
    rect = drawRect(side,side,pictureFile)
    return rect
#set up function to draw triangle
def drawTriangle(side,pictureFile):
    for i in range(side):
        for j in range(i+1):
            print("*",end="", file=pictureFile)
        print(file=pictureFile)
#create a menu to keep asking if data is entered incorrectly
def menu():
    choice = "No"
    while not(choice == "r" and choice == "s" and choice == "t" and choice == "q"):
        choice = input("Enter choice: ")
        print("r for rectangle \ns for square \nt for triangle \nq for quit")
        return choice
    
def main():
    pictureFile = open("shapePix.txt","w")
    choice = "a"
    while choice != "q":
        choice = menu()
        if choice == "r":
            rdimen = input("Enter length, height: ")
            rList = rdimen.split(",")
            width = int(rList[0])
            height = int(rList[1])
            drawRect(width, height, pictureFile)
        elif choice == "s":
            side = int(input("Enter length of side: "))
            drawSquare(side, pictureFile)
        elif choice == "t":
            tdimen = int(input("Enter length of base: "))
            drawTriangle(tdimen, pictureFile)
            
    print("Your picture is now available on shapePix.txt")
    pictureFile.close()
main()