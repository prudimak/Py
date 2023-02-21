# def sum(num1,num2):
#     num3 = num1 + num2
#     print(num3)
# num1 = eval(input("Enter a number : "))
# num2 = eval(input("Enter a number : "))
# sum(num1,num2)
# replacing characters in a string
# num='mama'
# num.replace('a','e')
# print(num.replace('a','e'))
# new=input('What is your name? ')
# print('Hello there ' + new)
shopping={}
def enter():
        product=input('Enter product name: ')
        price=eval(input('Enter amount: '))
        shopping['product']=product
        shopping['price']=price
shopping[input('Enter product name: ')]= 'product'
shopping[eval(input('Enter amount: '))]= 'price'
def get_shopping():
    print(shopping)
enter()
get_shopping()
