addition = 2 + 3  + \
           5 + 5 +  \
           5 + 8 + \
           8 + 8 + 9
print(addition)

# new line continuation character
operators = 2 + 6 + 8 - 2 / 85 + 59 - 9 + 9 / 19 
print(operators)

operation = ( 8 + 9 - 7 +   # paranthesis
             7 + 10 + 20 +932 +
             85 +585 - 1449)
print(operation)

# mutliline statement in List 
list1 = ['Lalit',
         'Ram','Rohit','Rohan',
         'Amar','Shiv',]
print(list1)

dict = {'Lalit' : 4, 'Ram' : 5,
        'Rohit' : 7, 'Amar' : 2,
        'Shix' : 8}
print(dict)

# del statement

x = 10
y = 20
print(x,y)
# del x,y
print(x,y)

#  return statement 
def addition(num1,num2):
    return num1 + num2

print(addition(10,20))

#  import statement
import datetime
now = datetime.datetime.now()
print(now)
