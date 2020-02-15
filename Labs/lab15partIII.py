#Dounglan Cheung
#Lab15partIII
def processFile(fileName):
    sold = [0, 0, 0, 0]
    for obj in fileName:
        obj = obj.strip()
        if obj == "hammer":
            sold[0] = sold[0]+1
        elif obj == "wrench":
            sold[1] = sold[1]+1
        elif obj == "saw":
            sold[2] = sold[2]+1
        elif obj == "screw driver":
            sold[3] = sold[3]+1
    return sold

def fileName(m):
    months = ["January.txt", "February.txt", "March.txt", "April.txt", "May.txt"]
    return months[m-1]

def getValidMonth():
    monthNum = -1
    while not (monthNum > 0 and monthNum <= 5):
        monthNum = int(input("Enter a month number between 1 to 5: "))
    return monthNum

def printResults(items, sold):
    for i in range(4):
        print("{0:20}".format(items[i]), sold[i])

def main():
    number = getValidMonth()
    file = fileName(number)
    infile = open(file, "r")
    sold = processFile(infile)
    items = ["hammers", "wrenches", "saws", "screw drivers"]
    printResults(items, sold)
main()