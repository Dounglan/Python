#Dounglan Cheung
#AvgHighLow
def computeAvg():
    infile=open("Jan05temps.txt","r")
    count = 0
    sum = 0
    count=count+1
    temp = int(infile.readline())
    sum=sum+temp
    for line in infile:
        count=count+1
        temp=int(line)
        sum=sum+temp
    infile.close()
    average=sum/count
    return average

def findLow():
    infile = open("Jan05temps.txt","r")
    temp = int(infile.readline())
    low = temp
    for line in infile:
        temp = int(line)
        if temp<low:
            low = temp
    infile.close()
    return low

def findHigh():
    infile = open("Jan05temps.txt","r")
    temp = int(infile.readline())
    high = temp
    for line in infile: 
        temp=int(line)
        if temp>high:
           high = temp 
    infile.close()
    return high

def printResults(average, high, low):
    print("Average temperature: {0:.2f}".format(average))
    print("High temperature:", high)
    print("Low temperature:", low)
    
def main():
    average = computeAvg()
    high = findHigh() 
    low = findLow()
    printResults(average, high, low)
main()    