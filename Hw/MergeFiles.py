#Doung Lan Cheung
#Assignment 5, problem A
#Create input files for student names and scores. Make output for gradebook of students 
def main():
#get names    
    file_name = input("Enter a file name with .txt at the end: ")
    students = open(file_name, "r")
    students1 = open(file_name, "r")
    contentnames = students.readlines()
    cnames = students1.read()
    print(file_name)
    print(cnames)
    students.close()
#get scores    
    file_score = input("Enter a file name with .txt at the end: ")
    scores = open(file_score,"r")
    scores1 = open(file_score,"r")
    contentscores = scores.readlines()
    cscores = scores1.read()
    print(file_score)
    print(cscores)
    scores.close()
    a = len(contentnames)
#get outfile
    outfile= open("GradeBook.txt","w")
#separate the grades from list       
    for n in range(a):
        contentnames[n] = contentnames[n].rstrip("\n")
        contentscores[n] = contentscores[n].rstrip("\n")
        contentscores[n] = contentscores[n].split()      
#grab the first two numbers
    e1 = []
    e2 = []
    avg = []
    sum1 = 0
    sum2 = 0
    sumAvg = 0
    for first in contentscores:
        e1 = e1 + first[0:1]
        e2 = e2 + first[1:2]
#find the average of the two scores and find the overall average of all students    
    for num in range(a):
        e1[num] = int(e1[num])
        e2[num] = int(e2[num])
        avg = avg + [(float(e1[num]) + float(e2[num]))/2]
        sum1 = sum1 + (float(e1[num]))
        sum2 = sum2 + (float(e2[num]))
        sumAvg = sumAvg + avg[num]       
    sum1final = sum1/a
    sum2final = sum2/a
    sumAvgFinal = sumAvg/a
#print the table for grades    
    v = "Average"
    print("Gradebook.txt", file=outfile)
    for m in range(a):
        print("{0:<20}".format(contentnames[m]), "{0:10}".format(e1[m]), "{0:10}".format(e2[m]), "{0:20.2f}".format(avg[m]), file=outfile)
    print("{0:<8}".format(v), "{0:26}".format(sum1final), "{0:9}".format(sum2final), "{0:17.2f}".format(sumAvgFinal), file=outfile)
    outfile.close()
main()