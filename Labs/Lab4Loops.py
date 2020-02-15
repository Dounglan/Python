for k in range(4):
    print(k)
for i in range(6, 21, 3):
    print(i)
for t in [3,5.0,hello!,-6]:
    print(t)
for c in [2.0,3.0,4.0]:
    print(type(c))
sum = 0
for j in range(10,14):
    sum = sum + j 
    print(sum)
for k in range(200,193,-1):
    print(k)
mystery = 3
for k in range(40):
    mystery=mystery+10
print(mystery)
sum = 0
for a in range(1,31):
    sum = sum + a**2
print("Final sum: ",sum)
#PART IV of B
sum = 0
for b in range(40,101,2):
    sum = b**2 + sum
print(sum)

#PArt C of IV
sum = 0 
for c in range(1,101):
    sum = 1/c + sum
print("Final sum is :", sum)

sum = 0 
for c in range(1,1001):
    sum = 1/c + sum
print("Final sum is :", sum)