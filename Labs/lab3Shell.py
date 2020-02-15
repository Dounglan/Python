Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Dounglan/AppData/Local/Programs/Python/Python37-32/lab3StepThru.py 
x= 23
x= 24
New York
NewYork

Ha
Ha
Ha
Enter a whole number from 10 to 20: 19
Enter another whole number: 17
19 17
Enter your family name: Cheung
Your nmame is Cheung!!
>>> for i in range(4):
	print(i, end=" ")

	
0 1 2 3 
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i, end="Ho")

	
0Ho1Ho2Ho3Ho4Ho
>>> for range(5):
	
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i, end=" ")

	
0 1 2 3 4 
>>> for i in range(10):
	print(i, end=" ")

	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(0):
	print(i, end=" ")

	
>>> for i in range(-2):
	print(i, end=" ")

	
>>> list(range(4))
[0, 1, 2, 3]
>>> list(range(1))
[0]
>>> list(range(0))
[]
>>> >for i in [2, 4, 6, 23]:
 print(i, end=" ")
 
SyntaxError: invalid syntax
>>> for i in [2, 4, 6, 23]:
 print(i, end=" ")
 
2 4 6 23 
>>> >for i in range(5):
 print(2*i, end=" ")
 
SyntaxError: invalid syntax
>>> for i in range(5):
 print(2*i, end=" ")

 
0 2 4 6 8 
>>> for i in range(6):
 print(2*i, end=" ")

 
0 2 4 6 8 10 
>>> >for i in range(5):
 print(100+(2*i), end=" ")
 
SyntaxError: invalid syntax
>>> for i in range(5):
 print(100+(2*i), end=" ")

 
100 102 104 106 108 
>>> for i in range(6):
 print(100+(2*i), end=" ")

 
100 102 104 106 108 110 
>>> for i in range(6):
 print(1+(2*i), end=" ")

 
1 3 5 7 9 11 
>>> x = int(input("What is the value of x?"))
What is the value of x?0
>>> for x in range(5):
	print(
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> for x in range(5):
	print(x-1, end=" "))
	
SyntaxError: invalid syntax
>>> for x in range(5):
	print(x-1, end=" ")

	
-1 0 1 2 3 
>>> 
