'''.........Factorial of a number using recursion.......

function calls inside the function called recursive function'''

def factorial(num):

    if num <= 1:
        return num
    
    else:
        return num * factorial(num-1)

num = int(input('Enter a number:'))    
    
print('Factorial of the number is:',factorial(num))    