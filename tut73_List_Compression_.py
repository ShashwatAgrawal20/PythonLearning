# ------------------------LIST---------------------------





# ye jaruri nhi hai ki list ke hi comprision hote hai dictionary ke bhi hote hai compresions.. aur generator compresion bhi hoti hai 

#  Agr aapne ko koi aaisa banana hai ki vo numbers 3 se divisibals ho to aapan kuch iss tarah se banayaenge ...

# shashwat = []

# for i in range(100):
#     if i%3==0:
#         shashwat.append(i)
# print(f"The numbers in the range of 100 which are divisible by 3 are:-\n \n {shashwat}\n\n")

# saransh = []

# for i in range (500):

#     if i%4==0:
#         saransh.append(i)
# print (f"The Numbers which are divisible by 4 in the range of 500 are:-\n \n {saransh}")


# lekin ye hi aapan kuch chand hi lino me kr skte hai ye bhi bhot impornt hai .. chand mtlb ek hi line me ..uss ko list compresion bolte hai iss me short hand if else bhi use hote hai .. 


# ye jo list compresion ka jo syntax hota hai vo kuch iss tarah aata hai .. iss me pehele ek variable dalna hota hai aur uss ke bad ek square brackets .. uss ke bad for loops lagana hotahai aur uss ke bad jo hai vo if condition deni hoti hai .. aur ye optional hoti hai .. ye nhi bhi di to jo aapan ne likha hai vo list me aajata hai .. 
# ls = [i for i in range (100)]
# print(ls)

# ls = [i for i in range (100) if i%3==0]
# print(ls)


# -------------------DICTIONARY----------------------------




# suppose aapan ko dictionary me kuch iss tarah se kr na hai ki {1:"item0", 2:"item1", 3:"item3"}ye aapne ko 100 tak kr na hai to ek tarika hai ki iss ko pura likhte baithna aur ek tarika hai iss ko dictionary compresions ki mdt se krna .. 
# ye jo niche ka hai aapan kuch iss tarike se bhi kr skte hai iss ko .. 

# ye jo hai ye iss me hi mtlb dictionary me hi condition wala hai ye . 
# dict1 ={i:f"item{i}" for i in range(1001) if i%100==0}
# print(dict1)

# # ye jo hai ye bina if else wala hai bina condition wala hai ye.. 
# dict1 ={i:f"item{i}" for i in range(1001)}
# print(dict1)

# dict2 = {i:f"item{i}"for i in range (1, 11)}
# a = (dict2)
# print(a)

# ISS SE AAPAN DICTIONRAY KE KEY VALUE PAIRS KO BHI ULTA KR SKTE HAI . YE BHI KAM KA HAI BHOT .. ulta mtlb ye kuch iss tarah se ho jayenga .. pehele key thi aur bac me value thi to ye pehele value layengi aur bad me key dengi .. 


# dict1 = {i:f"Item{i}" for i in range(5)}
# dict1 = {value:key for key, value in dict1.items()}
# print(dict1)





# ---------------------SET COMPRESSION----------------------------


# dresses = {dress for dress in ["dress1", "dress3""dress1", "dress3""dress1", "dress3""dress1", "dress3""dress1", "dress3","dress1", "dress3""dress1", "dress3""dress1", "dress3", "dress1", "dress3""dress1", "dress3""dress1", "dress3"]}

# print(dresses)
# print(type(dresses))



# ----------------------generators compression-----------------


# for to make a generator compression we use ()
# list me bhi ye hi syntax hota hai bas uss me aapan square brackets use kr te hai .. 
evens = (i for i in range (100) if i%2==0)
print(type(evens))

for i in evens:
    print(i)

