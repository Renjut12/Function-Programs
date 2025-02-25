'''......Check whether the a number is odd or even .........?'''

def check(num):
    
    return (num % 2 == 0)
    
num = int(input("Enter number:"))

if(check(num)==True):
      
      print("Number is even...!")

else:
      print("Number is odd....!")