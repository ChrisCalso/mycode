
#! /usr/bin/env python3

def calculate():
    operation = input('''type in the math operation you would like to complete-->
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    num1 = float(input('enter the first number: '))
    num2 = float(input('enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    else:
        print('NOT a  valid operator, please run the program again.')

calculate()
