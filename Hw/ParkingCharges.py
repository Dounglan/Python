#ParkingCharges.py
#aString consists of the ID number and the number of
#minutes, all in one string.  White space separated.
#Returns a list.
#  The first item is the ID number (as a string, no
#  white space before or after)
#  The second item is the number of minutes, and int.
def processString(aString):
    a = aString.split()
    list = [a[0], int(a[1])]
    return list
#mins is the the number of minutes, an int.
#Computes and returns a float, the charges
#   in dollars (and cents)
def computeCharge(mins):
    charge = ((mins//60.0)*3.50) + ((mins%60.0)*0.10)+2.0
    return charge
#outfile is the file, already opened.
#goodList is a list.
#The first item is a string,
#   the ID number,
#The second item is the number of minutes, an int.
#charge is the charge
#Print the ID #, the number of minutes, and the charge,
#   laid out to be under the header lines.
#Prints to both the monitor and the file outfile
def printALine(outfile, goodList, charge):
    print(goodList[0], goodList[1], charge)

def main():
    #Open input and output files.
    infile = open("garageData.txt","r")
    outfile = open("garageRecords.txt","w")
    #Initialize the total income for the day.
    total=0
    #Print headers to both the monitor and the output file.
    print("{0:<10}{1:>10}{2:>10}".format("ID #","minutes","charge"), file=outfile)
    print("{0:<10}{1:>10}{2:>10}".format("ID #","minutes","charge"))
    #Read the header line from the input file
    infile.readline()
    #Process each data line in the input file.
    for line in infile:
        goodList = processString(line)
        charge=computeCharge(goodList[1])
        total=total+charge
        printALine(outfile, goodList, charge)
    #Print the total income to both the monitor and the output file.       
    print("Total:{0:24.2f}".format(total), file=outfile)
    print("Total:{0:24.2f}".format(total))
    #Close the input and output files.
    infile.close()
    outfile.close()
main()    