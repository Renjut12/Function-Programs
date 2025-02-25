'''.......Define a function in python that accepts 3 values and returns the maximum of three numbers....?'''


def maximum (x,y,z):

    
    if (x > y) and (x > z):
        return x

    elif (y > x) and (y > z):
        return y

    else:
        return z
    
x = int(input('Enter first number:'))
y = int(input('Enter second number:'))
z = int(input('Enter third number:'))

largest = maximum(x,y,z)

print( 'Maximum of three numbers=', largest)


'''.........Using function..................'''



# def largest_number(a, b, c):
#     list = [a, b, c]
#     return max(list)

# a = int(input('Enter first number:'))
# b = int(input('Enter second number:'))
# c = int(input('Enter third number:'))

# Largest = largest_number(a,b,c)

# print('Maximum of the given three numbers is =',Largest)   




