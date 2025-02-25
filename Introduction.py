'''    Basic of functions       '''

''' functions are Four types.........

    1. Built-in function      ( print() , input() )
    2. User defined function  
    3. Recursive function
    4. Lambda function.........
     
      Function  :   A function is a block of code which only runs when it is called  
      
      code reusability is possible .................'''

# General format of function.........

# def function_name():
#    block of code .............>  function definition
# function_name()  .............>  function calling 

# def one():
#    print("Welcome to python world......!")

# one()
# print('Hai')
# print('Hello')
# one()

#............ Arguments and Parameters........

#def functionname(param1,param2):
#   block of code
# functionname(arg1,arg2)

''' Arguments:-
 Information can be passed into functions as arguments, 
 they are specified as the function name inside the paraenthesis , 
 you can add as many aruguments as you want just seperate them with comma, 
 it is the value that is send to the function when it is called .
 A parameter is variable listed inside the paranthesis in the function definition....'''

# def addition(a,b):
#     print("sum is: ",a+b)

# addition(10,20)
# addition(15,5)   



# documentation string....

# def hello():

#      ''' It is just statement-docstring or documentation string'''

#     print("Welcome to function")

# hello()
# print(hello.__doc__)    


''' Python documentaion string assossiating documention with function, classes and methods. 
 it is used to like a comment to document a specific segment of code'''


'''...........Required arguments........'''

# def display(name,age):
#     print("name is: ",name,"age is:",age)

# display("Ammu",20)
# display("Ajay",34)    

'''.........Default arguments.........'''

# def display(name,age=30):
#     print("name is:",name,"Age is:",age)
# display("Ammu",20)
# display("Ajay")
# display("Amal")    



'''by default a function must be called with the correct number of arguments meaning that if your functionexpect two arguments you have to call with two arguments not more  

If we call thw function it uses the default argument  '''


'''.........Arbitary arguments(*args) - variable-length arguments .......'''

# def newfunction(*kids):
#     print(kids)
#     print("The youngest child is ",kids[0])
# newfunction("Ajay","Amal","Amith")
# newfunction("Ajay","Amal","Amith","Akhil","Ammu")

# if you don't know how many arguments that will be passed into your function add a * before the parameter name in the function definition this way the function will recieve a tuple of arguments and can access the items accordingly.......


'''........Keyword Arguments (kwargs).........'''

# def display(child2,child3,child1):
#     print(child2)
#     print(child3)

# display(child1="Ammu",child2="Anju",child3="Akhil")    
    

# you can also send arguments into the key value syntax this way the order of the arguments does not matter,    

'''....Arbitary keyword arguments (**kwargs).......'''

# def display(**child): # ( ** used for dictionary format)
#     print(child)
#     print(child['child1'])

# display(child1="Ammu",child2="Anju",child3="Akhil",child4="Athira")    

# if you don't know how many keyword arguments that will passed into your function 



'''.....Return statement.......'''

# def addition():
#     return

# print(addition(8,7)) 
    
    # ............Local Scope and Global Scope...........


# the return keyword is used to exit function end return a value statement after the return line will not be executed return statement is used to end the execution of the function call and returns the value of the expression following the return keyword to the caller , if the return statement is without any expression  then the special value non is returned it is overall used to so that the passed statement can be executed 


# Local scope: A variable created inside afunction belongs to and can only be used inside the function...
# Python local variables which are defined inside the the function and their scope is limited to that function only
# it can not be accessed anywhere out side the function

# A variable created in the main body of the and belongs to the global scope 
# Those which are defined outside any function and which are accessible throught the program that is inside and outside of every function

 #......... Local variable.........

# def hello():
#    a = "apple"
#    print(a)

# hello()
# print(a)




#.............Global variable.......

# a = "apple"
# def hello():
#     print(a)

# hello()
# print(a)

# ..........global keyword..........

# if we need to create a global variable but are stuck in the local scope you can use the global keyword....
# the global keyword makes the variable global, Also use the global variable if you want to make a chane to a global variable inside a function

# a = 10
# def hello():
#     global a
#     a+=2
#     print(a)

# hello()
# print(a)


# ...........pass........

# def hello():
#     pass

# hello()





'''..............Recursion............'''

''' Recursion is acommon programming concept it means that a function calls it's self. This has the benifits of meaning that you can loop through that can reach a result'''


# def hello(num): # num=5 num=4 num=3 num=2 num=1 num=0
#     if num<=0: # 5<=0 4<=0 3<=0 2<=0 1<=0 0<=0
#         return num
    
#     else:
#         return num + hello(num-1)   # 5+hello(5-1)    5+hello(4)
#                                     # 5+4+hello(4-1)  9+hello(3)
#                                     # 9+3hello(3-1)    12+hello(2)
#                                     # 12+2+hello(1)    
#                                     # 15 + hello(0)
# print(hello(5))


'''....Lambda functions.......

Lambda functions are anonymous function that can pass any number of arguments and only one expression......'''

# def sum(a,b):
#     print(a+b)
#     print(a-b)

# sum(2,4)

# variable_name = lambda arguments:expression

''' A lambda function is anonymous function , a lambda function can take any number of arguments but can only have one expression. The expression is executed and a result is returned '''
''' Anonymous function means that the function is without a name'''



# x = lambda a,b,c : a+b+c
# print(x(3,4,2))

'''.........Lambda function with condtional statements.........'''

# n = lambda x:"positive" if x>0 else "negative" if x<0 else "zero"

# print(n(5))
# print(n(-5))
# print(n(0))


'''.............Lambda function methods..........'''
# filter , map , reduce

'''...Filter method...'''

# x = [1,2,3,4,5,6,7,8,9,10]
# y = list(filter(lambda z:z%2==0,x))  # z is an argument
# print(y)

'''...write a program to print even numbers between 1 and 100 using lambda function with filter method.....'''

# y = list(filter(lambda z:z%2==0,range(1,101)))
# print(y)

'''.............Map method.............'''

'''.....Write a program to print the square of the numbers in between 1 and 50 using lambda function map method....'''
# y = list(map(lambda z:z**2,range(1,51)))
# print(y)

'''....Write a program to convert given lowercase words to uppercase value using lambda function map method....''' 

# fruits = ['orange','mango','apple']
# x = list(map(lambda y:y.upper(),fruits))     # y is an argument
# print(x)

'''................Reduce method.................'''

# from functools import reduce
# z = [1,2,3,4,5]
# x = reduce(lambda a,b:a+b,z)
# print(x)


# x = reduce(lambda a,b:a+b,range(1,101))
# print(x)

''' Filter method : A filter function in python takes in a function list as argument this offers an elagant filter out all the elements of a sequence for which the function returns to true

Map method : The map function in python takes in afunction and list as an argument , the function is called with a lambda function and a new list is returned which contained all the lambda modified item returned by that function for each item 

Reduce Method : The function is called with a lambda function and an iterable and  a new reduced result is returned, This performs a repeatative operation over the fairs of the iterable.... '''
