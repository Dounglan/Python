#Doung Lan Cheung
#DataConverter.py
def main():
#Ask for the date    
    months="JanFebMarAprMayJunJulAugSepOctNovDec"
    k = input("What is the date in mm/dd/yy separated by forward slashes?")
#Grab first two characters from the date string, change them into int and use that number for month    
    month = int(k[0:2])
    pos = 3*(month-1)
    monthAbbrev=months[pos:pos+3]
#Grab the 2 characters for the day, turn them in to int and use it as the day
    day = int(k[3:5])
    years = k[6:8]
    yr = "20"+years
    year = int(yr)
#print the date in abbreviated month, day, yyyy    
    print(monthAbbrev+".",day,",",year)
main()