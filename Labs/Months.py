#Doung Lan Cheung
#lab8
def main():
    longMonth=["January","February","March","April","May","June","July","August","September","October","November","December"]
    month= eval(input("What is the month number?"))
    days= ['31','28','31','30','31','30','31','31','30','31','30','31']
    print(longMonth[month-1],"has", days[month-1],"days")
main()