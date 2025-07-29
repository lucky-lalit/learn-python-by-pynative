# addition operator
x = 4
y = 2
print(y**x)
print(x + y)

x = 'Lalit '
y = 'Tiwari'
print(x + y)

# substraction operators

x = 20
y = 30
print(x - y)

# Multiplication operators

x = 2
y = 10
z = 15
print(x * y *z)

# Division

x = 63
y = 5
print(x / y)
print(x % y)
print(x // y)

# comparision operator
x = 10
y = 5
z = 2

# > Greater than
print(x > y)  # True
print(x > y > z)  # True

# < Less than
print(x < y)  # False
print(y < x)  # True

# Equal to 
print(x == y)  # False 
print(x == 10)  # True 

# != Not Equal to 
print(x != y)  # True 
print(10 != x)  # False 

# >= Greater than equal to
print(x >= y)  # True
print(10 >= x)  # True

# <= Less than equal to
print(x <= y)  # False
print(10 <= x)  # True

a = 4
b = 2

a += b
print(a)  # 6

a = 4
a -= 2
print(a)  # 2

a = 4
a *= 2
print(a)  # 8

a = 4
a /= 2
print(a)  # 2.0

a = 4
a **= 2
print(a)  # 16

a = 5
a %= 2
print(a)  # 1

a = 4
a //= 2
print(a)  # 2
# print(0 and 1)

print(True and False)  # False
# both are True
print(True and True)  # True
print(False and False)  # False
print(False and True)  # false

# actual use in code
a = 2
b = 4

# Logical and
if a > 0 and b > 0:
    # both conditions are true
    print(a * b)
else:
    print("Do nothing")

print(True or False)  # True
print(True or True)  # True
print(False or False)  # false 
print(False or True)  # True

# actual use in code
a = 2
b = 4

# Logical and
if a > 0 or b < 0:
    # at least one expression is true so conditions is true
    print(a + b)  # 6
else:
    print("Do nothing")

print(not False)  # True return complements result
print(not True)  # True return complements result

# actual use in code
a = True

# Logical not
if not a:
    # a is True so expression is False
    print(a) 
else:
    print("Do nothing")

my_list = [1,2,3,4,5,6,7,8,9]
number = 5
if number in my_list:
    print('number is present')
else:
    print('number is not present')

my_list = [1,2,3,4,5,6,7,8,9]
number = 50
if number in my_list:
    print('number is present')
else:
    print('number is not present')

x = 10
y = 11 
z = 10
print(x is y) # it compare memory address of x and y 
print(x is z) # it compare memory address of x and z

x = 10
y = 11 
z = 10
print(x is not y) # it campare memory address of x and y 
print(x is not z) # it campare memory address of x and z

a = 7
b = 4
c = 5
print(a & b)
print(a & c)
print(b & c)

a = 7
b = 4
c = 5
print(a | b)
print(a | c)
print(b | c)

a = 7
b = 4
c = 3
print(~a, ~b, ~c)

print(4 << 2) 
# Output 16
print(5 << 3)
# Output 40

print(4 >> 2)
# Output 
print(5 >> 2)
# Output 

a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)

x = (1, 2, 3)
y = (1, 2, 3)
print(x == y)
print(x is y)