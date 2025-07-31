# roll_no = 33
# # display roll no
# print("Roll number is:", roll_no)  # 33
# print(type(roll_no))  # class 'int'

# # create integer using int() class
# id = int(25)
# print(id)  # 25
# print(type(id))  # class 'int'

# # print(len(roll_no))
# print(' ')
# print('#####################################################')
# print(' ')
# import cmath
# phi = cmath.phase(complex(-1.0,1.0))
# print(phi)

# c = cmath.rect(1)
# print('real:',c.real)
# print('imag:',c.imag)
# print('complex::',c)

# p =cmath.polar(c)
# print('polar::',p)

# print(' ')
# print('###############################################')
# print(' ')

# i = 10
# print('The integer in octadecimal::',oct(i))
# print('The integer in hexaecimal::',hex(i))

# print(' ')
# print('###############################################')
# print(' ')

# # Implicite and Explicite
# x = 99
# y = 1.65
# z = x + y
# print(type(z))

# s = 'Hello'
# m = 33
# print(s+str(m)) 

# print(' ')
# print('###########################  math module methods ############################')
# print(' ')

# import math as m
# a = 1.4
# print(m.ceil(a))
# print(m.floor(5.9))

# print(m.pi)
# print("Degree value of pi is ::",m.degrees(m.pi))
# print("Radian value of 90 degree is ::",m.radians(90))
# print(' ')

# # sin() and cos()

# print(m.cos(m.radians(180)))
# print(m.cos(m.degrees(180)))
# print(m.cos(m.radians(60)))
# print('debug1',type(m.sin(m.radians(90))))

# print(' ')
# print('#################### facotrial')
# print(' ')

# print('The Factorial of the number is: ',m.factorial(4))

# print(' ')
# print(m.fabs(-15.06592))
# print(m.trunc(-15.06598))
# print(m.fabs(-15))
# print(type(m.trunc(15.54)))

# print(' ')
# print(' ')
# print(type(m.pow(4,2)))
# print(type(m.log(2)))

# print('')
# print('**************************************')
# print('')

# print(m.isfinite(m.inf))
# print(m.isinf(m.inf))  ##########################################################################################

# # print(m.isnan(dffg))
# print(m.isnan(25454))
# print(m.isnan(m.nan))

# print('')
# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
# print('')

# print(m.isclose(1.5,7.6))
# print(m.isclose(1.5,2.5))
# print(m.isclose(1.4,2.5,abs_tol=1.0))
# print(m.isclose(2.1,2.5,rel_tol=11))

# print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

# print(m.sqrt(25))
# print(m.lcm(20,5))
# print(m.gcd(12,18))
# print(m.exp(-2))
# print(m.pow(4,2))

# x = 5.67
# print(x.is_integer())
# print(x.as_integer_ratio())

# print('')
# print('######################### Decimal Module ############################')
# print('')

# import decimal
# from decimal import *
# print(Decimal(0.01))
# print(Decimal(123))
# print(Decimal('123'))
# print(Decimal('0.01'))
# # print(Decimal((1, (9,9,9,9), -2)))
# print(Decimal((1,(9,9,9,9),-2)))

# print(Decimal(3)/Decimal(77))
# getcontext().prec = 4
# getcontext().rounding = decimal.ROUND_DOWN
# print(Decimal(3)/Decimal(77))

# import decimal
# from decimal import Decimal, getcontext
# getcontext().clear_flags()
# print(Decimal(2).sqrt())
# print(' ')
# print('#########################################')
# print('')

# from fractions import Fraction #,Decimal
# print(Fraction(25, -100))
# print(Fraction('-3/7'))

# from decimal import Decimal
# print(Fraction(Decimal('9.9')))

# from decimal import Decimal
# print(Fraction(9.1))

# Fraction()

# import fractions
# f = Fraction(m.pi).limit_denominator(100)
# print('The Fraction created::',f)
# print('Numerator::',f.numerator)

# print(Fraction.from_float(0.25))
# print(Fraction(300,124))

# print("Total 6 digits with 4 after the decimal point :::")
# print('{:09.4f}'.format(1.141592653589793))
 
# print("6 digits including the sign:::")
# print('{:=10d}'.format((- 234)))

# print('')
# print("with relative difference < difference::", m.isclose(5,1.75,rel_tol=0.5))


i=-99
print("bit length::", i.bit_length())
print(bin(i))

# import decimal
# from decimal import Decimal, getcontext
# getcontext().clear_flags()
# print(Decimal(2).sqrt())
# import math
# print(1.060000)
# print(f'{1.060000:6.4f}')
# # print(abs(-45.300))
# print(math.fabs(-45.300))
# print(f'{(abs(-45.300)):6.3f}')
# a = 42e3
# print(type(a),a)

# print(round(100.2563, 3))
# print(round(100.000056, 3))
# print(f'{round(100.000056, 3):3.1f}')
# print(f'{round(100.000056, 3):3.3f}')
# print(f'{round(1.000056, 3):3.0f}')
# print(round(100.2563, 3))
# print(round(100.000056, 3))
# print(round(100.2563, 3))
# print(round(100.000056, 3))