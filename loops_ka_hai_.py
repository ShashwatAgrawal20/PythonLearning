'''
# iss me aapan loops ka use kr ne wale hai

# List1=["Harry", "Larry", "Carry", "Marie"]

# print(List1[0], List1[1])    # ye thoda biginner method hai.. agr aapne ko list ko acces kr na hai to .........

# aab advance method hai ye ................

# for item in List1:
#     print(item)     # iss se aapan ek br me list ke pure elements access kr skte hai ye bhot imp chij hai........

# iss ke mdt se aapan tuple ko bhi kr skte hai ......
  

list1=[ ["Harry", 1], ["Larry", 2] , ["Carry", 6] ,  ["Marie", 250 ] ]
dict1=dict(list1)
print(dict1)
for item, lollypop in list1:
    print(item,"and lolly is: ",lollypop)  # is ko aapan iteresion bolte hai ...

list1=[ ["Harry", 1], ["Larry", 2] , ["Carry", 6] ,  ["Marie", 250 ] ]
dict1=dict(list1)
print(dict1)
for item, lollypop in  dict1 . items():  # iss ke kam ka hota hia .items() function
    print(item,"and lolly is: ",lollypop)   # iss me aapan ne ye dictionary ke madat se kiya hai ye bhi imp function hai for loop ka iss ko dhyan me rakhna 


for item in dict1:
    print(item)  # iss se sirf items hi print hote hai ye bhi kam ka hai yad rakhna hai iss ko bhi ..


# iss ka use aapan if else me bhi kr skte hai ....

items=[int,float,"shashwat",3,3,44,66,3,2,44,77,0,111,333,44,4,6]

for item in items:                # ye loops ko aapan ne sort kr ne ke lye use kya hia ye bhot imp hia .......
    if str(item) .isnumeric()and item>=6:
        print(item)

# ye bhot kam ka hai iss me bhot kuch hai loops ke bre me ...  # ye bhot imp hai seriously ....

# iss me ek hota hai while loops .......
a=input()

'''
# ye while loops ka bs itna hi tha bas ho gya hai ye sb.......loops khatm

# yha se pura aapan while loops ka krenge ye kam ka hai ... pura ka pura page ....

i=0
while (i<500):  # ye chalta jayenga kyuki aapan ne iss ko kha hai jb tak i <46 tb tak i ko hi print kr na hai to ye vo hi krenga
    print(i)
    i=i+1  # ye statement ke karan aappan ne numbers print krvai iss se kha ki i me jo i hai aur 1 jod do uss ne vaisa hai kiya aur aapne ko numbers mile ....
