#NestedLoops.py
#Dounglan Cheung
#part c
#for row in range(10, 50, 10):
#    print("row :" ,row, "\t", "columns: ",end = "\t")
#    for col in range(1, 4, 1):
#        print(col, "\t", end ="\t")
#    print("\n")

#part d
#for row in range(10, 50, 10):
#    for col in range(1, 4, 1):
#        sum = row + col
#        print(sum, end =" ")
#    print("\n")
#part e
for row in range(0, 80, 10):
    print(row, end=" ")    
    for col in range(1, 10, 1):
        sum = row + col
        print(sum, end =" ")
    print("\n")
#partIV
for row in range(1,8,1):
    for col in range(ord('A'), ord('G')):
        print(str(row)+chr(col), end=" ")
    print("\n")
    