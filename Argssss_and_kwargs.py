'''
def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)
function_name_print("Harry", "Rohan" ,"Shashwat", "Anand", "gandu ")

# yha se real function chalu hota hai .. 

def gandu (*args):
    print(type(args))

    # ye universal type ka hota hai 
halkat =["gandu ", "halkat", "gandu ", "kutta","dukkar"]    
print(*halkat) # agr aapan ne *aur jis me aapan ne likha hai vo likha to ye bhi kam krdenga.. mtlb ye unlimited type ka hojayenga jaisa aapna ko agr iss ke upar wale iss me dala to ye aapan ne jitne elemet define kre hai utnehi kam aayege {aapane ko dono me * lagana pdta}  {{{ye tuple ke rup me jayenga.. }}}

'''
'''
# iss ke bare me ke funfact hai aapan iss ko args ko koi bhi nam se pukar skte hai means kuch bhi nam de skte hai jase argsshashwat to bhi ye program aache se run honga aur koi bhi dikkat nhi denga.. 
def kutta (nromal,*argsshashwat):
    print(normal)
    for item in argsshashwat:
        print (item)
# iss ka bhi vohi faida hai aapan iss me forloop bhi laga skte hai ye bhi vaise hi kam krta hai aur aapan iss me upar wale program ki tarah add bhi krskte hai chije.. !!!Important..  aapan iss me ek aur aurgument bhi de skte hai jaise iss me normal diya hai .. 


chickoo = ["you", "I", "My","Me", "We", "Our", "Us"]        
normal = "I am a normal aurgrument and this are some preposition:"
kutta(normal, *chickoo)
'''
# !!! Important = aapen ko normal ko pehele rakhna hai aur uss ke bad agrs ko rakhna hai aur uss ke bad          agr aapan ne ye sequence follow nhi ki to ye error throw krenga.. 



# YHA SE KWAGRS KA CHALU HOTA HAI .. 



def kutta (nromal,*argsshashwat,**kwargsbala):
    print(normal)
    for item in argsshashwat:
        print (item)
    print("\nNow I would like to intorduce the heroes")
    for key , value  in kwargsbala.items():
        print(f"{key} is a {value}")

chickoo = ["you", "I", "My","Me", "We", "Our", "Us"]        
normal = "I am a normal aurgrument and this are some preposition:"
kw = {"rohan":"monitor", "shashwat":"Timepass", "chickoo":"gandu ","cook":"shivam"}
kutta(normal, *chickoo, **kw)
# YE JO ARGS ARU KWARGS HOTE HAI YE OPTIONAL HOTE HAI DENA HAI TO DO NHI DENA HAI TO REHENE DO AGR AAPAN NE YE LAST STATEMENT ME SE ,*chickoo HTA DIYA TO BHI YE ERROR THROW NHI KRNEGA.. 