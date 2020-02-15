#Doung Lan Cheung
#dcheun01@syr.edu
#Assignment 2, problem 2.
#February 1, 2019
#Ask the user for how many pairs of points and compute the distances.
import math
def main():
#Ask for how many pairs of points and for the x and y cooridinates    
    pts = eval(input("Enter how many pairs of points: "))
    for a in range(pts):
        x, y = eval(input("Enter x and y cooridinates separated by a comma"))
        x2,y2 = eval(input("Enter x and y cooridinates separated by a comma"))
        d= math.sqrt((x2-x)**2+(y2-y)**2)
#print the how many pairs of points, starting and ending points and the distance.
        print("How many pair of points?",pts)
        print("start point - ",x,",",y)
        print("end point - ",x2,",",y2)
        print("Distance: ",d)
main()