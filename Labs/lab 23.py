#Dounglan Cheung
#Lab23
#4/29/19
def power(a,n):   #part I
    if n == 1: #base
        ans = 1
    else:
        ans = a * power(a,n-1) #recursion step
    return ans

def sumIterative(n):  #part IIa
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

def sumRecursive(n):  #part IIb
    if n == 0:
        ans = 0
    else:
        ans = n + sumRecursive(n-1)
    return ans

def square(n):
    if n == 1:
        ans = n #base case
    else:
        ans = (n-1)**2+(n-1)+n #recursive statement
    return ans

def main():
    x = power(2,6)
    print(x)
    alist = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]
    for i in alist:
        num = pow(i,5)
        print(num)
    
    sum = sumIterative(5)
    print(sum)
#part IIb
    Rsum = sumRecursive(5)
    print(Rsum)
#part IIc
    for k in [1,5,10,100]:   #iterative
        Isum = sumIterative(k)
        print("Iterative sum of k: ", k, Isum)
    for k in [1,5,10,100]:
        Rsum = sumRecursive(k)
        print("Recusive sum of k: ", k, Rsum)
#part III
    for i in range(1,21):
        sum = square(i)
        print("Square of "+str(i)+ ":", sum)
main()