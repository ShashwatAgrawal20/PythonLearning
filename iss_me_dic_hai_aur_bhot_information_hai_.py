                # bhot imp thing is that list =[] ,,, tuple =()aur dictionary ={} ye ek dam aache se yadd rakh na hai 
        

d1={"Good bye":"Adieu","To get wet":"Drench","Flexible":"Agile ", "The feeling that this incident already occured in past":"Dijauv",
    "Kidnaped":"Abduct"}

print("shashwat sir enter the word you want to know \n")  # ye thoda alg hai ye aaise hi dictionary bna di thi maine 
d1.update({"halkat":"gandu "})
# d1=["gandu "],"chickoo"

#  iss me del function bhi use hota hai jaise aapne ko koi remove marna hai dic me se to del d1 [jo nam kr na hai vo [Good bye ]] to Good bye del ho jayenga
# ek aur fun reheta hai jaise aapan ne d2=d1 kr dya hai aur iss me se koi remove mra  to vo d1 me se bhi remeove ho jayenga [iss lye d2=d1.copy kr ke likhna ]

name =input()
try:
    print ("Shashwat sir your required word is = ",( d1 [name]))
except Exception as e:
    print (e)    
print ("Thanks sir for using our dictionary")

# iss me add kr ne ka tarika hai d1="gandu ","Chickoo" ye bhi ek tarika hai kr ne ka 
# aur aacha tarika hai d1.update({"gandu ":"Chickoo"})     lekin jadatar ye hi tarika use kr na chiyea..........................]]]]}}}}}}}}}}}
# print (d1.keys())       # to iss se jo aapan ne pehele nam likhe hai vo print ho jayenge  ................
# print (d1.items())      # iss se jo key value pairs hai vo print hote hai dono chije words bhi aur meaning bhi  hai vo print hote hai dictionary me ...........



                              #  yha se dusra chalu hota hai list vgre aache se dekhna hai 


grocery=["Harpic", "Vimbar", "deodrant", "bhindi", "lollypop",56]
print(grocery[1])

numbers=[2, 7, 9, 11, 3]
print(type(numbers))# ye ek list hai ye bhot kam me aati hai .......
print(numbers)
numbers.sort()# ye no ko aapne dam pe chote se bde ke iss pe sort kr ta hai 
print(numbers)
# numbers.reverse()  # ye numbers ki list ko ulta kr deta hai 
print (numbers)
print(max(numbers))  # max no print kr ta hai 
print(min(numbers))  # min no pritn kr ta hai 
numbers.append(67)   # last me no aad kr ta hai {iss ka english me mtlb hai ki last me }
print (numbers)
numbers.insert(1,3)  # iss ka mtlb hai ki bich me khi pr insert kr de na hai ye no { pehele no pr index ka nam dalna hai ki konse iss ke 
                     # bad aapne ko aad kr na hai no aur dusre no pe kya no dalna hai }
print (numbers)

# Mutable = the words that can be changed
# immutable = the words that cannot be changed

                     #    iss me ek prakar aata hai tuple means ye inmutable hai aur jo list reheti hai vo mutable hoti hai

tp = (1,2,3)
print (tp ) # agr mai iss ko change kr ne dalung to ye error mrega 

                                 # ek aur chij jo dhyan dene lyak hai ki

a=1
b=8 # agr aapne ko inn dono ko swape kr na hai to sbse easy ninja technique 
print (a,b)
a,b=b,a
print (a,b)  # lge to run kr ke dhek lena smj me aa jayenga hua ki nhi hua lekin comma jarur lagana .........


# DICTIONARY HAI YE AUR USS KE FUNCTION HAI ISS ME
a=input()

