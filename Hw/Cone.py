#Doung Lan Cheung
#Computes the surface area and volume of a cone with inputs of r and h
import math 
def main():
# Ask for the height and radius of the cone
    h = eval( input( "Enter the height of the cone: "))
    r = eval(input("Enter the radius of the cone :"))
#State and compute the volume and surface area
    V= (1/3)*math.pi*(r**2)*h
    SA= math.pi*r*(r+ math.sqrt(h**2+r**2))
#Print the volume, surface area, radius, and height
    print("Radius: ",r)
    print("Height: ", h)
    print("The volume is ", V, "cubic units")
    print("The surface area is ", SA, "square units")
main()
