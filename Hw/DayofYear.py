#Official Name: Doung Lan Cheung
#email: dcheun01@syr.edu
#Assignment: Assignment 4, problem 1.
#Date:February 18, 2019
#Figuring out what day of the year and week, given the date is through input
def main ():
    monthLengths=[31,28,31,30,31,30,31,31,30,31,30,31]
    d = input("What is the day of the week in mm/dd/yyyy? ")
    month = int(d[0:2])
    day = int(d[3:5])
#use a loop and monthLengths to figure out the day of the year
    start = 0
    for n in monthLengths[:int(month)-1]:
        start = start + n
    start = start + day
    print(d,"is day",start,"of the year.")
    print("1 for Sunday")
    print("2 for Monday")
    print("3 for Tuesday")
    print("4 for Wednesday")
    print("5 for Thursday")
    print("6 for Friday")
    print("7 for Saturday")
#Ask user for number for what the day will be for Jan. 1    
    dayofw = int(input("What day of the week is Jan 1? (Enter a number) "))
    weekdays=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    DaY = start//7
    DAY = weekdays[((start+dayofw)%13)-2]
    print(d, "falls on a",DAY)
main() 