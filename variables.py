name = "John"  # string assignment
age = 25  # integer assignment
salary = 25800.60  # float assignment

print(type(name),name)  # John
print(type(age),age)  # 25
print(type(salary),salary)  # 25800.6
#################################################################
var = 10
print(var)  # 10
# print its type
print(type(var))  # <class 'int'>

# assign different integer value to var
var = 55
print(var)  # 55

# change var to string
var = "Now I'm a string"
print(var)  # Now I'm a string
# print its type
print(type(var))  # <class 'str'>
#######################################################################

# change var to float
var = 35.69
print(var)  # 35.69
# print its type
print(type(var))  # <class 'float'>

# create a variable of type string
str = 'PYnative'
# prints complete string
print(str)  # PYnative

# prints first character of the string
print(str[0])  # P

# prints characters starting from 2nd to 5th
print(str[2:5])  # nat

# length of string
print(len(str))  # 8

# concatenate string
print(str + "TEST")  # PYnativeTEST

########################################################
my_list = [12,10.5,12,'Hello','Ram']
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[1:3])
my_list[0] = 'Lalit'
my_list.append(1000)
print(my_list)  

##########################################################
my_set = {'Emma', 'Jessa', 'Kelly'}
print(my_set,type(my_set))
print(type(my_set).__name__)

########################################################3
a = 100
A = 200

# value of a
print(a)  # 100
# Value of A
print(A)  # 200

a = a + A
print(a)
#################################################

import constant

print(constant.PI)
print(constant.TOTAL_AREA)

a = b = c = 10
print(a) # 10
print(b) # 10
print(c) # 10

roll_no, marks, name = 10, 70, "Jessa"
print(roll_no, marks, name)

#####################################################3
def test1():  # defining 1st function
    price = 900  # local variable
    print("Value of price in test1 function :", price)

# def test2():  # defining 2nd function
    # NameError: name 'price' is not defined
    # print("Value price in test2 function:", price)

# call functions
test1()
# test2()

################################################
price = 900  # Global variable

def test1():  # defining 1st function
    print("price in 1st function :", price)  # 900

def test2():  # defining 2nd function
    print("price in 2nd function :", price)  # 900

# call functions
test1()
test2()

n = 300
m = n
z = m
z = 400
print(id(n)) # same memory address
print(id(m)) # same memory address 
print(id(z))

a = 10
b = 10
print(id(a))
print(id(b))

c = 20
d = 20
e = 20
print(id(c))
print(id(d))
print(id(e))
# ###############################################
import sys
print(sys.getrefcount(a))
print(sys.getrefcount(c))
###############################################
a = 10
b = 10
c = 20
d = 20
e = 20
tupel1 = a,b,c,d,e 
list1 = a,b,c,d,e######################
print(tupel1)
print(list1)################

a,b,c,d,e = tupel1
print(a,b,c,d,e)