Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Dounglan
>>> area=3*4
>>> area
12
>>> length = 7
>>> width=5
>>> area = length*width
>>> area
35
>>> length = 10
>>> area
35
>>> area = length*width
>>> area
50
>>> 
=============================== RESTART: Shell ===============================
>>> area
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    area
NameError: name 'area' is not defined
>>> 27
27
>>> apples=6
>>> apples
6
>>> oranges = "navel"
>>> oranges
'navel'
>>> 3.14159
3.14159
>>> type(apples)
<class 'int'>
>>> type(oranges)
<class 'str'>
>>> type(3.14)
<class 'float'>
>>> type("something in quotes")
<class 'str'>
>>> print(234)
234
>>> print(apples)
6
>>> print(oranges)
navel
>>> print("I like" + oranges)
I likenavel
>>> name = input("What is your name")
What is your nameD
>>> name = input("What is your name?")
What is your name?Dounglan
>>> name
'Dounglan'
>>> length = input("What is the rectangle's length?")
What is the rectangle's length?2
>>> width = input("What is the rectangle's width?")
What is the rectangle's width?3
>>> width = int(input("What is the rectangle's width?"))
What is the rectangle's width?3
>>> length =int(input("What is the rectangle's length?"))
What is the rectangle's length?2
>>> area = length*width
>>> area
6
>>> perimeter = length+width
>>> perimeter
5
>>> print("Hi " + name)
Hi Dounglan
>>> print(Your rectangle has area + str(area))
SyntaxError: invalid syntax
>>> print("Your rectangle has area" + str(area))
Your rectangle has area6
>>> print("Your rectangle has area " + str(perimeter))
Your rectangle has area 5
>>> 
====== RESTART: C:/Users/Dounglan/Documents/ECS102/ProcessRectangle.py ======
What is your name?Dounglan Cheung
What is the rectangle's length?2
What is the rectangle's width?3
Hi Dounglan Cheung
Your rectangle has area 6
Your rectangle has area 5
>>> 
========== RESTART: C:/Users/Dounglan/Documents/ECS102/milesToKM.py ==========
Enter distance in miles: 1
1 miles equals 1.609 kilometers
>>> 
========== RESTART: C:/Users/Dounglan/Documents/ECS102/milesToKM.py ==========
Enter distance in miles: 1
1 miles equals 1.609 kilometers
>>> miles
1
>>> 
========= RESTART: C:/Users/Dounglan/Documents/ECS102/milesToKMv2.py =========
Enter distance in miles: 1
1 miles equals 1.609 kilometers
>>> main()
Enter distance in miles: 2
2 miles equals 3.218 kilometers
>>> 
========= RESTART: C:/Users/Dounglan/Documents/ECS102/milesToKMv3.py =========
Enter distance in miles: 1
Enter distance in miles: 2
Enter distance in miles: 3
Enter distance in miles: 4
4 miles equals 6.436 kilometers
>>> 
