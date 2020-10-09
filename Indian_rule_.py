'''                                         # set ka hai ye 
#  ye bhi bhot imp chij hai                                         

s=set()
print (type (s))
numbers =[1, 2, 3,]
print (numbers)
s.add(1)
s.add(2)
print(s)
s.union({1,2})
print(s)
s.remove (1)
print (s)

                                       # if else condition  (this is a very important function)

var1=6
var2=56
print("iss me (56) se compare kiya hai ")
print("sir please enter the number")

var3 = int(input() )

if var3>var2:
    print ("Greater")

elif var2==var3:
    print("Equal")
     
else:
    print("Lesser")

l=[3,4,2,1]

print(3 in l)
'''
while (True):   
    print("Sir please enter your age \n ")
    age=int (input())
    if age>18 and age <101:
        print("Chala bhai teri iccaha lekin licence hona jaruri hai \n")
    elif age> 0 and age <18:
        print("Rehane de bhai tuzse na ho pye ga \n  ") 
    elif age==18:
        print("Test ke lye aa iccha hui to denge \n ")
    elif age>151:
        print("Bs ha dada kyu phirki le rhe ho subah se koi nhi mila kya ..   { ht sale meri iccha hi nhi hai taiko bta ne ki bhg .. jaldi ... !!!!! }\n ")
        break    
    else:
        print(" Bs ha dada bhto jee lye dusro ko bhi jeene dete ki nhi re baba .. .. !!!  \n ") 
        
        





    
