# Official Name:Doung Lan Cheung
# email: dcheun01@syr.edu
# Assignment: Assignment 4, problem 2.
# Date: February 14, 2019
# a program that asks for the principal, the annual rate and the number of payments. You will then print the monthly breakdown, in a beautifullyformatted table like the following
def main():
    princ = int(input("Principal: "))
    air = eval(input("Annual Interest Rate: "))
    month = int(input("How many months is the loan? "))
    rate = (air/100)/12
    monthlypay = princ*rate/(1-(1+rate)**(-1*month))
    print("Principal {:8.2f}    ".format(princ),"     Monthly Payment  {0:0.2f}".format(monthlypay),"\nAnnual Interest {0:5.1f}%".format(air),"      Term        ",month, " months")
#creat and print the table
    print()
    print("Payment","      ","Interest","     ","Pay to Principal","   ","Balance")
    for i in range(1,month+1):
        interest = float(rate*princ)
        paytoprinc = float(monthlypay-interest)
        princ = float(princ - paytoprinc)
        print(i,"\t\t  ", "{0:0.2f}".format(interest),"\t\t   ","{0:0.2f}".format(paytoprinc),"\t  ","{0:0.2f}".format(princ))
    print("Due: ", "{0:0.2f}".format(princ))
main()