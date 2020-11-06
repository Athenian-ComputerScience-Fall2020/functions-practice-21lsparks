'''
Collaborators: 
# megan leich
'''


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


num1 = int(input("Enter a number or die: "))
num2 = int(input("Enter a number or die: "))

tomato = int(input("For adding, type 1, subtraction = type 2, multiplication = 3, division = 4:  "))

if tomato == 1:
    print(add(num1, num2))
elif tomato == 2:
    print(sub(num1, num2))
elif tomato == 3:
    print(mult(num1, num2))
elif tomato == 4:
    print(div(num1, num2))