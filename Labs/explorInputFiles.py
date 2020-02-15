#exploreInputFiles.py
#Exploring reading a file with different string methods
def main():
      # PART A
    infile=open("fruit.txt","r")
    contentsString=infile.read()
    print(contentsString, type(contentsString))
    infile.close()
      # PART B
#    infile=open("fruit.txt","r")
#    contentsList=infile.readlines()
#    print(contentsList)
#    infile.close()
      # PART C
#    infile=open("fruit.txt","r")
#    aLine = infile.readline()
#    print("A: ",aLine,type(aLine))
#    aLine = infile.readline()
#    print("B: ",aLine,type(aLine))
#    aLine = infile.readline()
#    print("C: ",aLine,type(aLine))
#    infile.close()
    # PART D
#    infile=open("fruit.txt","r")
#    for line in infile:
#        print("Line:" , line,type(line))       
#    infile.close()
main()    
    