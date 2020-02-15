#squaresAndCubes.py
#Dounglan Cheung
#Ask user for 2 pos. int, m,k
m, k = eval(input("Enter two positive integers, separated by a comma"))
a = m-1
#Print the squares of the numbers from 0 to m-1, separated by spaces

for x in range(a):
    x = x**2
    print(x, end=" ")
    
#Print the cubes of the numbers from 1 to k+1, separated by commas
#Can you do it so there's no comma at the end?
print()
for y in range(1,k+1):
    y= y**3
    print(y, end=",")
print((k+1)**3)
