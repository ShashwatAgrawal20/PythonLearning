# F STRINGS..

# iss se aapan ek string ke andar ek variable use krskte hai ye kam ka hai bhot..

'''
# ye wala aapne ko use nhi krna hai 
me = "Harry"
a = "this is %s"%me
print(a)
'''

# ye niche wala bhi thoda thik thak hai ek iss se bhi aacha tarika hai iss me vo use kr na hai .. 
'''
# ye nya hai string formatting me ..
me = "Shashwat"
a1 = 3
a = "chickoo gandu hai {} {}"
b = a.format(me, a1)
print (b)

me = "Shashwat"
a1 = 3
a = "chickoo gandu hai {1} {0}" # to ye jo a1 hai uss ko 1 me fit krdenga aur jo me hai uss ko 0 me kr denga.. 
b = a.format(me, a1)
print (b)
'''


# YHA SE F STRING CHALU HOTA HAI 



# aapan iss me function ko import se bhi krskte hai 
import math
me = "chikna"
a1 = 3
a = f"This is {me} {a1} {4*25}''' agr aapan ne koi function import krke bhi likhaa to ye aapane ko de denga jaise aapan me math ko import kra aur iss ne aapen ko ye de diya jaise hi aapan ne f string me iss ki value dali hai  '''{math.cos(65)}" # ye f string aaise kam kr ti hai iss se aapan aapne iss ko redable bana skte hai f string ke mdt se aapen ko bas jo likhna hai vo likhna pdta hai aur uss ke bad kya lagana hai vo likhna hota hai .. 
print (a)