'''
# def print2(str1):
#     print("This is " + str1)
# print2("shashwat")



# def print2(str1):
#     print2(str1)  #agr aapane ne iss ke andar ye hi lga diya to ye uss ke andar jata jayenga jata jayenga aur khatam hi nhi honga..ye recurssion error denga ..  
#     print("This is " + str1)
# print2("shashwat")

# yha se recursion ka use chalu hota hai ye bhot kam ka hai 



# Factorial ka function chalu hota hai yha se ye bhi kam ka hai ye internative hai 
 

def Factorial_iterative(n):
    """Takes a integer
    return : n*n-1*n-2*n-3........"""
    # for example 5 ka hota hai 125

# n! = n*n-1.........1
# n! = n* (n-1)!

    fac = 1
    for i in range(n):
        fac = fac*(i+1)

    return fac

# this is a recursive function
    
def factorial(n):
    if n==1:
        return 1
    else : 
        return  n*  factorial(n-1)


number = (int (input("Enter the number which you want to get a factorial : ")))    
print("Factorial using recursive meathod .. ", Factorial_iterative (number))    
print("Factorial using recursive meathod .." , factorial(number))








# From here the quiz starts..


# Fibonacci sequence{{0, 1, 1, 2, 3 }} first to iss ki addition hota hai fibonacci number

def fibonacchi (n):
    if n == 1: 
        return 0
    elif n==2:
        return 1    
    else:
        return fibonacchi(n-1)+fibonacchi(n-2)  
s = (int(input("Enter the number")))
print ("fibbonacchi of number is ", fibonacchi(s))
'''

def hypo(a,b):
    if a ==1 and b==1:
        return 1
    elif a==0 and b==0:
        return ("an error occur") 

    else:
        return ((s**2)+(a**2)) //(2)
        

          


s = (int(input("Enter the number  ")))  
a = (int(input("Enter the number  ")))  
try:
    print("Hypoteneous :", hypo(s,a))
except Exception as e:
    print(e)
    










