'''
a=10
b=5
c= sum ((a, b))  # iss me tuple hona ya list hona chiyea tabhi ye kam krta hai .. 
# ye hote hai built in functions .....
print(c)

# aur ye honge user define functions .. jo user denga uss ko... .. 
# ye koi bhi input nhi le rha hai .. ye wala function .. . 

def function1 ():
    print ("Hello you are in function 1")
print (functions1()) # agr print lagai to none aa rha hai aur agr nhi lgai to nhi aayega 
functions1() # jaise ki iss me nhi aaya sirf function 1 likha to ......



def function2 (a, b):
    print ("Hello you are in function 2", a+b)
# ye value iss ne tamiz se nhi di hai .. iss ko aapan variable me store nhi kr skte hai ..

function2(5, 6) 


def function3 (a, b):
    average=(a+b)/2
    print(average)
v = function3 (5, 7)   # iss ne aabhi aapne ko kuch bhi nhi diya thenga diya hai iss ne .. .. ye none show krenga .....   
print(v)

iss me ye return aur input dena optional ho skta hai ... 
def function4 (a, b):
    average=(a+b)/2
    print(average)     # ek bar iss ki vajah se print hua hai 6.0
    return average     # return se aapan koi bhi iss me store kr skte hai ye chije .... jaise aab iss ne vo value variable me store krdi hai .. . 


v = function4 (5, 7)   # iss ne aabhi aapne ko kuch bhi nhi diya thenga diya hai iss ne .. .. ye none show krenga .....    
print(v)               # dusri bar iss ke vajah se print hua hai 6.0


iss me ye pehele v= function 4 se jayenga phir vo def me ghusenga .. uss ke bad vo average return kr enga uss ek bad vo 
phir se aapni v= {wali line me aajayenga aur phri vo uss me store kr ke print kr denga value ....... iss tairke se ye sb work kr ta hai .... ye --
-- function aur return value aur ye def wala iss se aapan aapna khud ka function bhi bna skte hai .. ye bhot kama ka hai re baba .. }


def function5 (a, b):
    average=(a+b)/2
    # print(average)     # ek bar iss ki vajah se print hua hai 6.0
    return average     # return se aapan koi bhi iss me store kr skte hai ye chije .... jaise aab iss ne vo value variable me store krdi hai .. . 

#  aabh ek hi bar hongi 6.0 ki value ... 
# iss me input dena aur return likhna optional ho skta hai ......
# program yha se chalu honga aur vo v ki value 5 aur 7 leke def me jayenga .. aur ye execute karenga .......
v = function5 (5, 7)   # iss ne aabhi aapne ko kuch bhi nhi diya thenga diya hai iss ne .. .. ye none show krenga .....    
print(v)               # dusri bar iss ke vajah se print hua hai 6.0
'''
# yha se dogstring chalu hota hai .. jo code me ki peheli line hoti hai uss ko dogstring bolte hai ... vo aapan as a print statement bhi use hoti hai ..


  # function contain dogstring........

def function5 (a, b):
    """This is the function which will calculate the average of two numbers
    This function dosent work for three work ... ye sirf 2 no ke sath he use honga...."""
    average=(a+b)/2
    # print(average)     # ek bar iss ki vajah se print hua hai 6.0
    return average 
print (function5.__doc__)  # iss se aapna dog string print kr skte hai.... ye line se functoinn me peheli string doc string hoti hai....
print(function5.__doc__)
print (function5(5, 5) )  


def halkat(str):
    print(str, "I have already printed the thing ")
    return str
v = halkat(str )
print(v)


   
