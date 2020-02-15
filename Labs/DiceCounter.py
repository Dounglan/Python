#Dounglan Cheung
#lab16
#DiceCounter
from random import randrange
def roll():
    r = randrange(1,7)
#    print(r, end=" ")
    return r

def main():
    ones = 0
    twos = 0
    threes = 0
    counter = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(1000):
        red = roll()
        green = roll()
        r = red + green
        counter[r] = counter[r]+1
#        if r == 1:
#            ones = ones + 1
#        elif r == 2:
#            twos = twos + 1
#        elif r == 3:
#            threes = threes + 1
#    print("\n",ones,twos,threes)
#    print("\n",counter)
#partD
    count = 0
    for value in counter:
        print(count, value)
        count = count + 1
main()