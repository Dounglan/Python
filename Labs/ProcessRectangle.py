#ProcessRectangle.py
#by Dounglan Cheung
#Compute the area and perimeter of a rectangle
#Ask for name
name = input("What is your name?")
#Ask for length and width
length = int(input("What is the rectangle's length?"))
width = int(input("What is the rectangle's width?"))
#Compute the area and perimeter
area = length*width
perimeter = 2*(length+width)
#Print results
print("Hi " + name)
print("Your rectangle has area " + str(area))
print("Your rectangle has area " + str(perimeter))
