'''
Adapt the code from one of the functions above to create a new function called 'multiplier'.
The user should be able to input two numbers that are stored in variables.
The function should multiply the two variables together and return the result to a variable in the main program.
The main program should output the variable containing the result returned from the function.
'''


def multiplier(num1, num2):
    return num1 * num2

if __name__ == '__main__':
    num1 = 0
    num2 = 0
    while num1 == 0 or num2 == 0:
        try:
            num1 = int(input('Enter a number or live.'))
        except:
            print("Hahaha, sucka.")
        try:
            num2 = int(input("Enter a number or your dog will fart"))
        except:
            print("You are dumb.")
    print(multiplier(num1, num2))
