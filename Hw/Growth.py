#Doung Lan Cheung
#dcheun01@syr.edu
#Assignment 2, problem 3.
#February 1, 2019
#Write a program that will compute all 3 of these values for values of x, starting with x=0,up through x=30. In steps of 5. Ask the user for the value of a
def main():
#set x equal to zero and ask for a value for variable a.
    x=0
    a = eval(input("Enter a value: "))
    st = 1000
#print a row for whatever the table requires    
    print("x     1000+ax    x^a      a^x")
    for x in range(0,31,5):
#Do z equals whatever the value a is with x multiplied together.        
        z = a*x
        c = st + z
        d = x**a
        e= a**x
#print x, 1000+ax, x^a, a^x.
        print(x,"   ", c,"     ", d,"      ",e)
main()