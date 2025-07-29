import keyword
import datetime
print(keyword.kwlist)

# print(help('if'))

print(keyword.iskeyword('if'))
print(keyword.iskeyword('range'))
print(keyword.softkwlist)

x = 10
y = 20
z = x < y
print(z)

if x > 5 and y < 25:
    print(x + 5)

if x < 10 or y < 25:
    print(x + 5)

if not x:
    print(x + 5)

print(x is y)
print(x is not y)

my_lsit = [1,2,3,4,5,6,7]
print(15 in my_lsit) 

x = 75
if x > 100:
    print('x is greater than 100')
elif x > 50:
    print('x is greater than 50 but less than 100')
else:
    print('x is less than 50')

for i in range(5):
    print(i,end = ' ')
    # break
print(f'answer using while loop')
num = 0
while num < 5:
    print(num, end = ' ')
    num = num + 1
print(f'def structure')
def addition(num1,num2):
    return num1 + num2
print(addition(10,20))

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(self.name,self.age)

#     # def show(self):
#         # print(self.name, self.age)

# s =student('Jessa',15)
# s.show()    

current = datetime.datetime.now()
print(current)
# 
# form math import math.pi
price = 900  # Global variable

def test1():  # defining 1st function
    print("price in 1st function :", price)  # 900

def test2():  # defining 2nd function
    print("price in 2nd function :", price)  # 900

# call functions
test1()
test2()

# delete variable
del price
# test1()
print('################################################')
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name,self.age)

    def show(self):
        print(self.name, self.age)


# create object
s = Student('Jessa', 19)
print(id(s))
# s = Student('Jessa', 19)
print(id(s))
# call method
s.show()
s.show()
s.show()
s.show()

from datetime import datetime

# get current datetime
now = datetime.now()
print(now)

import sys
print(sys.getrefcount(s))
t = s
print(sys.getrefcount(s))
print(sys.getrefcount(t))
u = Student('pushpendra',25)
print(sys.getrefcount(s))
print(sys.getrefcount(t))
print(sys.getrefcount(u))

print('###################################################')
# l = m = n = 85921730
l = 859217309
# m = l
# n = m
print(sys.getrefcount(l))
# print(sys.getrefcount(m))
# print(sys.getrefcount(n))
