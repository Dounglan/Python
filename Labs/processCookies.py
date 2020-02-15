#processCookies.py
#Obtain information from the file cookieSales.txt.
#Print how many kids there are and their names.
#Print the total number of Samoas sold.
def main():
#open the input file
    infile=open("cookieSales.txt","r")
#read the file into a list inputList
    inputList=infile.readlines()
#compute how many kids there are
    numLines=len(inputList)
    numKids=(numLines-3)//2
    print("There are " + str(numKids) + " kids selling cookies.")  #notice str
#print the names of all the kids and compute the Samoas sales.
    sumSamoas=0   
    for i in range(3,numLines,2):
        a = inputList[i]
        print("{0:<15}".format(a)) ##why empty lines?
        #print(inputList[i].rstrip())  ##one trick to learn
        salesLineList = inputList[i+1].split()
        sumSamoas=sumSamoas + int(salesLineList[1])   #notice int
#Susie
    name = inputList[3].rstrip()
    salesLineList = inputList[4].split()
    print("{0:<19}||{1:>26}  |{2:>33} |{3:>40}  ||".format(name, salesLineList[0], salesLineList[1], salesLineList[2],))
    print("There were {0} boxes of Samoas sold.".format(sumSamoas))
#close the file
    infile.close()
main()