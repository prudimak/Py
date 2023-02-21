# dot syntax
# import operators
# x=operators.add(12,34)
# print(x)
# y=operators.subtract(45,89)
# print(y)

# from operators import add
# x=add(23,45)
# print(x)
# from operators import subtract
# y=subtract(89,34)
# print(y)

# import others
# x=others.cube(9)
# print(x)
import operators
import others
import trig
operator=input('Enter operator: ')
if operator=='*3':
    num=eval(input('Enter number: '))
    x=others.cube(num)
    print(x)
elif operator=="sin":
    angle=eval(input('Enter angle in degrees: '))
    sin_of_angle=trig.get_sine(angle)
    print(sin_of_angle)
elif operator=="cos":
    angle=eval(input('Enter angle in degrees: '))
    cos_of_angle=trig.get_cos(angle)
    print(cos_of_angle)
elif operator=="tan":
    angle=eval(input('Enter angle in degrees: '))
    tan_of_angle=trig.get_tan(angle)
    print(tan_of_angle)
    
else:
    num1=eval(input('Enter number 1: '))
    num2=eval(input('Enter number 2: '))
    if operator=='+':
        x=operators.add(num1,num2)
        print(x)
    elif operator=='-':
        x=operators.subtract(num1,num2)
        print(x)
    elif operator=='/':
        x=operators.divide(num1,num2)
        print(x)
    elif operator=='*'or'x'or'X':
        x=operators.multiply(num1,num2)
        print(x) 
    




