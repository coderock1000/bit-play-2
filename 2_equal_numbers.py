def checkifsame(num1, num2):
    if ((num1 ^ num2) != 0):
        print('numbers are not equal')
    else:
        print('both numbers are equal')

num1 = int(input('Enter first number to compare: '))
num2 = int(input('Enter second number to compare: '))

checkifsame(num1, num2)