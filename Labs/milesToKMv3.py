# mileToKMv3.py
# your name
# Converts distance in miles to kilometers
def main():
    for i in range(4):
    # Ask for the distance in miles
        miles = eval( input( "Enter distance in miles: "))
    # Convert to kilometers
    km = miles * 1.609
    #Print the result
    print(miles, "miles equals", km, "kilometers")
main()
