# learningIf.py
def main():
    #Determine if of legal drinking age
    age = int(input("How old are you? "))
    checkLegal(age)
    
    #Determine the sign of a number
    x = float(input("Enter a real number." ))
    theSign = sign(x)
    print("The sign of " + str(x) + " is " + theSign)
    
    #Play fickle pickle
    guess=int(input("Enter a five digit number: "))
    if guess == 58329:
        print("Congratulations! You win a jar of pickles!")
    print("Thank you for playing fickle pickle.")        
#speeding    
    speed = int(input("What's your speed?"))
    checkspeed(speed)
#odd or even    
    date = int(input("What is the day of the month?"))
    day = date%2
    checkday(day)
#grades
    grade = int(input("Enter your grade out of 100: "))
    checkgrade(grade)
    #end main
# Check if of legal drinking age
# input parameter age
# no return value
# prints output
def checkLegal( age):
    if age >= 21 :
        print("Legal")
    else:
        print("Underage.\nPlease go home.")
# Determine the sign of a number
# input parameter x
# returns the sign, a string
# no printed output
def sign( x ):
    if x>0 :
        return '+'
    elif x == 0 :
        return '0'
    else:
        return '-'
def checkspeed(speed):
    if speed > 55:
        print("You are speeding.")
    else:
        print("You are under the speed limit.")
def checkday(day):
    if day == 0:
        print(day)
    else:
        day == 1
        print(day)
def checkgrade(grade):
    if grade >= 90:
        print('A')
    elif grade >= 80:
        print('B')
    else: grade < 80
    print("No credit")
main()      
          