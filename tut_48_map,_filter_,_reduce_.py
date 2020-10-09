# --------------map-------------
'''
map function kisi bhi chij ko list me krdeta hai .. 
numbers = ["3", "34", "64"]
# ye for loop ke jagah aapan map function ka bhi use krskte hai vo one liner hota hai .. 
# iss me aapan ko first aurgument me vo dena hai jo ki aapan chate hai ki sb pr apply ho jaye aur dusra vo dena hai jo aapan chate hai ki kis pr ho lekin agr aapan iss ko aaisa likhenge to ye error throw krdenga..    map(int, numbers)
# map ye ek object hota hai .. 
# agr work krana hai to aapane ko ye likhana hoga ...
numbers = list(map(int, numbers))



# for i in range (len(numbers)):
#     numbers[i] =  int (numbers[i])

numbers[2] = numbers[2]+1    
# print(numbers[2])

# def sq(a):
#     return a*a
# num = [2, 3, 5, 3, 33, 53, 32 ,3234, 33, 2424]
# square = list(map(sq, num))
# print(square)


num = [2, 3, 5, 3, 33, 53, 32 ,3234, 33, 2424]
square = list(map(lambda x :x*x, num))
print(square)


# iss ke upar tak ke map funciton hai

'''
'''
    
def square(a):
    return a*a 
def cube(a):
    return a*a*a

func = [square, cube]        
# num = [2, 3, 5, 6, 76, 3, 3, 2]
# ye niche wale me aapan ne function banaye aur uss ko map diya val dalke aur uss me ke lambda funciton diya aur bola ki agr tumhe x mile to tum ko kya kr na hai tum ko xi kr na hai aur kis me krna hai to func me krna hai aur print (val ) kr diya .. 
for i in range(25):
    val = list(map(lambda x: x(i), func))
    print(val)
# video is pending..  
'''
# --------------Filter-------------------


# Filter function starts from here.. 


# Filter function filter the things.. ye ek element ki aaisi list banata hai jiss me given funcion true return krta ho.. 
# iss se bhi aasan bhasha me bolu to ye filter jo hai vo alg kr ke deta hai.. chat kr deta hai .. 


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def is_greater_5(num):
#     return num>5
# ye hota hai filter function
# iss me aapan ne ek list di pehele list1 nam se phir ek funciton bnaya hai is_greater_5 nam se uss me aapan ne likha hai agr num hai vo agr 5 se bda hai .. aur phir aapan ne ek aur variable banaya hai gr_than_5 nam se iss me aapan ne filter function lagaya hai pehele nam function ka diya hai aur dusra wala list ka diya hai aur iss ko list me typecast krdiya .. aur phir print kr diya .. 

# gr_than_5 = list(filter(is_greater_5, list1))
# print(gr_than_5)


# ----------------------REDUCE----------------------

# reduce ye ek func tool module ka part hai agr aapan aaise hi likhenge to ye kuch bhi nhi honga .. aapne ko aaise likhna honga.. 
# from functools import reduce

from functools import reduce
list1 = [1,2,3,4, 2]
# num = 0
# for i in list1:
#     num = num +i
# print(num)

# iss me aapan pehela aurgument denge jo aapan krna chalte hai .. jaise ek function..aur dusra aurgument vo dena hai jis me aapan krna chate hai ye sb.. map ki trhh---------- ye bhot kam me aata hai ye oneline me bhi hota hai iss me aapa kuch bhi laga skte hai .. 
num = reduce(lambda x, y: x+y,list1 )
mul = reduce(lambda x, y: x*y,list1 ) # jaise aapan ne iss me ye multiply kiya hai aur aapan ye process ko REDUCE bolte hai .. 
print(num)
print(mul) 
# ye upar wala bhi vohi print kr enga jo aabhi niche wala krenga.. 



# aapne ko ek aase jadu ki jarurat hai jo 1ko 2 me jode 2 ko 3 me jode 3 ko 4 me jode aur maiko return kr de jo  bhi value hongi vo .. to iss kam me use hota hai reduce.. 


# ye iss lye use hote hai .. jo one lines ke lye use hote hai aur ye kbhi kbhi samne wale ne use kra honga aur .. uss ke lye aapne ko ye aane ko hona iss lye bhi hai ye .. 

