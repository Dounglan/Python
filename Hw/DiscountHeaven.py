#Doung Lan Cheung
#dcheun01@syr.edu
#Assignment 2, problem 1.
#February 1, 2019
#Print the number of items and then calculate the prices and then print my bill
def main():
    print("Discount Heaven where the prices will make you smile!")
    print("For each item, enter the number, then press enter.")
#input number of tires, soup bowls, hats, skate boards, pillows
    t = eval(input("Enter the number of tires: "))
    s = eval(input("Enter the number of soup bowls: "))
    h = eval(input("Enter the number of hats: "))
    sb = eval(input("Enter the number of skate boards: "))
    p = eval(input("Enter the number of pillows: "))
    ti = t+s+h+sb+p
#Enter price formulas for the amount you entered
    tp= (139.99*(t%4))+(420.00*(t//4))
    sp= (((s//6)*10.00)+((s%6)*1.88))
    hp= (10.50*(h//2))+((h%2)*7.00)
    sbp= (120.00*(sb//3))+((sb%3)*49.99)
    pp= (21.00*(p%4))+(80.00*(p//4))
    total = tp+ sp+ hp+ sbp+ pp
#print the bill
    print("Tires: ", t)
    print("Soup bowls: ",s)
    print("Hats: ", h)
    print("Skate boards: ", sb)
    print("Pillows: ", p)
    print("Your bill")
    print("******************")
    print("Tires","       ","$",tp,"  ",t)
    print("Soup bowls","  ",'$',sp,"  ",s)
    print("Hats","        ","$",hp,"    ",h)
    print("Skate boards","","$",sbp,"   ",sb)
    print("Pillows","     ","$",pp,"   ",p)
    print("-------------------------------------------")
    print("Total","       ","$",total,"   ",ti,"items")
    print("Come Again!")
main()