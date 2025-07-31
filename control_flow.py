number = 6
if number > 5:
    print(number*number)
print('The next line of code')

print('')
print('#############################')
print('')

# password = input('Enter the password: ')
# if password == '123456Enter':
#     print('Correcct Password')
# else:
#     print('Incorrect Password')

print('')
print('#############################')
print('')

def user_check(choice):
    if choice == 1:
        print('LALIT')
    elif choice == 2:
        print('AMAR')
    elif choice == 3:
        print('RAHUL')
    else:
        print('Wrong entry')

print(user_check(1))
print(user_check(5))
print(user_check(3))
print('')
print('#############################')
print('')

# num1 = int(input('Enter the 1st num: '))
# num2 = int(input('Enter the 2nd num: '))
# if num1 >=num2:
#     if num1 == num2:
#         print(num1,'is equal to',num2)
#     else:
#         print(num1,'is grater')
# else:
#     print(num2,'is grater')
print('')
print('#############################')
print('')

number = 56
if number > 0: print('Positive')
else: print('Negative')

x = 5
while x > 0: print(x,end=' '); x=x-1; print(x)
print('')
print('#############################')
print('')
for i in range(1,11):
    print(i)

num = 10
sum = 0
i = 1
while i <= num:
    sum=sum+i
    i = i + 1
print(sum)

for i in range(10):
    if i > 5:
        print('Stop the process:.')
        break
    print(i)

for i in range(3,8):
    if i == 5:
        continue
    else:
        print(i)

months = ['Jan','Feb','Mar','Apr','May']
for month in months:
    pass
print(months)
