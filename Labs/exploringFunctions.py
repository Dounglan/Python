#exploringFunctions.py
#Doung Lan Cheung
# Study RETURN VALUES and FORMAL PARAMETERS/ ARGUMENTS in functions.
def main():
    # Part B
    # comment 1
    #divAndMod (89,5)
    # comment 2
    #rewriter('w')
    # comment 3
    #triple(3.2)
    
    # Part C
    # comment 4
##    x = triple(1.1)
##    print("x= {0:.2f}".format(x))
    # comment 5
##    a = rewriter('w')
##    print("\na = ",a)
    # comment 6
##    r = divAndMod(100,9)
##    print(r)
    # Part D
    # comment 7
##    y=2.1
##    x=triple(y)
##    print("x = {0:.2f}".format(x))
##    print("y = {0:.2f}".format(y))
    # comment 8
##    n=23
##    d=10
##    r=divAndMod(n,d)
##    print("r =",r)
##    print("n =",n, "d =", d)
    # comment 9
##    s = "potato"
##    rewriter(s)
##    print("\ns =",s)
    # Part E
    rewriter('*')
    rewriter('$')
    rewriter('N')
    n = 13
    d = 5
    a = 15
    print("\nDividing", n, "by", d, end=":")
    r = divAndMod(n,d)
    print("{0:>34}{1:>2}".format("The remainder is ",r))
    #print("The remainder is ",r)
    print("\nDividing", a, "by", d, end=":")
    y = divAndMod(a,d)
    print("{0:>34}{1:>2}".format("The remainder is ",y))
    print()
    print()
    rewriter('+-+-')
    z=11.1
    x=triple(z)
    print("\nWhen I triple some number I get", x)
    print()
    rewriter('e')
    print()
    print(" ",end="")
    rewriter('c',)
    print()
    print("  ",end="")
    rewriter('s')
    print()
    # end main()
    
# Print the parameter 5 times.
# Does not advance to the next line.
# let is the formal parameter
# let is a string
def rewriter( let):
    print(let*5, end="")
# triple the number n.
# n is the formal parameter.
# Note, no printed output.
def triple(n):
    answer = 3.0 * n
    return answer
# end triple

# print num // den
# returns num % den
# num and den are formal parameters, should be int
def divAndMod( num, den ):
    quotient = num // den
    remainder = num % den
    print("The quotient is {0}".format(quotient))
    return remainder
# end divAndMod
