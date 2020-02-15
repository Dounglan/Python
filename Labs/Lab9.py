#Doung Lan Cheung
#Lab9.py
def main():
#PART 1
#Read a phrase    
#    word = input("Enter a phrase: ")
#Compute the average word length
#    length = word.split()
#    a = len(length) #how many words there are
#    b = len(word)-(a-1) #how many letters there are(want it w/o spaces)
#    c = b/a 
#Print the result
#    print(c)
#PART 3
#prompt user for the name of an input file
#    files = input("What is the name of the file(with .txt included)? ")
#open file for input
#    infile=open(files,"r")
#read the file using a "for line in a file" loop, print the line
#    for line in infile:
#        print("Line:",line)
#for each line, print and compute the average word length for that line
#        length = line.split()
#        a = len(length)
#        b = len(line)-(a)
#        c = b/a
#        print("Line:",line, c)
#close the input file
#    infile.close()
#PART 4
#    files = input("What is the name of the file(with .txt included)? ")
#    infile=open(files,"r")
#    content=infile.readlines()
#    for i in content:
#        length = i.split()
#        a = len(length)
#        b = len(i)-(a)
#        c = b/a
#        print(i, c)
#PArt 5 
    files = input("What is the name of the file(with .txt included)? ")
    infile=open(files,"r")
    write = infile.readlines()
    fil = input("What is the output file name? ")
    outfile=open(fil,"w")
    avg = 0
    sum = 0
    for line in write:
        words = line.split()
        numwords = len(words)
        numchar = len(line)
        sum = 0
        for i in words:
            sum += len(i)
        avg = sum/numwords
        print(line + str(avg), file= outfile)
    infile.close()
    outfile.close()
main()