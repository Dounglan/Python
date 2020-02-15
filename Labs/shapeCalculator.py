#shapeCalculator.py
from math import pi

def rectArea(length, width):
    area=length * width
    return area

def circleArea(radius):
    area=pi*radius*radius
    return area

def welcome():
    print("Welcome to the shape calculator!")
    name=input("What is your name? ")
    return name

def askDimension(dimension):
    value = float(input("what is the " + dimension +"? "))
    return value

def triangleArea(altitude, base):
    area = (altitude*base)/2
    return area    

def squareArea(side):
    area = rectArea(side, side)
    return area

def main():
    name = welcome()
    print(name+", ", end="")
    x = askDimension("length")  #enter 4
    y = askDimension("width")   #enter 3
    print("The area of the rectangle is " + str(rectArea(x,y)))
    rad = askDimension("radius")   #enter 10
    a= circleArea(rad)
    print("The area of the circle is {0:0.5} sq. cm.".format(a))
    alt = askDimension("altitude")
    base = askDimension("base")
    print("The area of the triangle is " + str(triangleArea(alt, base)))
    side = askDimension("side")
    print("The area of the square is " + str(squareArea(side)))
    dimList = [ 5, 3, 7, 2]
    first = dimList[0]
    print(squareArea(first))
    second = dimList[1]
    print(circleArea(second))
    third = dimList[2]
    fourth = dimList[3]
    print(rectArea(third, fourth))
main()