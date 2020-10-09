print("Hello World")

                               # faulty calclator hai ye .....................

print("Shashwat sir please enter your number")
n1=input()
print("Shashwat sir please enter the second number")
n2=input()



print ("sir enter the operation you want to do :",'+','-','*','/')
n3=input()

if n3=='+':
    print("Addition=")
    print(int (n1)+float (n2))
    
elif n3=='-':
    print("Subtraction=")
    print(int(n1)-float(n2))
elif n3=='/':
    print("Dividarion=")
    print(int(n1)/float(n2))
elif n3=='*':
    print("Multiplication=")
    print(int(n1)*float(n2))
else:
    print("Error (Check your number or operation...)")     
             
#  ye while loops ke iss se aapn ne calculator banaya ..........chota hi hai ye wala .. bs addition hi krta hai ......
while(True):
    ib=int(input("enter the second number .."))
    ia=int(input("enter the first number"))
    i=(input("enter the operation.. :\n"))
    if i=='+':
        print("your number is ",int (ia) + int (ib))
        break 
    elif i=='-':
        print("your subtraction is ", int (ia)- int )
   



