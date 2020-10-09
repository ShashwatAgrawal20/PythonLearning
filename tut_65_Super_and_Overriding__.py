class A:
    classvar1 = "I am a variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A constructor"
        self.classvar1 = "I am a instance variable in class A"
        self.special = "Special"

class B(A):
    classvar2 = "I am in class B"

# ye jo B me ka constructor hai ye override ho gya hai iss lye ye aabhi upar ke iss me nhi dhoond ta hai kyuki iss ko aapna khud ka variable mil gye to ye upar nhi jayenga balki iss me A ko bhi dala hai to bhi ye aapan ne purane iss me dheka hai .. 
    def __init__(self):
        # ye jo super hota hai ye aapane puranae iss ko run krne me mdt krta hai .. iss se aapan puranae iss ko acess kr skte hai .. jaise iss me aapan ne super lagake A ko acess kiya hai.. 
        # super().__init__()
        self.var1 = "I am inside class B constructor"
        self.classvar1 = "I am a instance variable in class B"
        self.Special = "special. "
        # agr ye bad me lagaya to ye change ho jate hai jaise iss me pehele iss ne iss ke lye aur phir iss ko super mil gya to iss ne A me ka print kr diya aaise work kr ta hai super aur overriding ka scene.. 
        super().__init__()
        print(A.classvar1)


a = A()
b = B()

print(b.classvar1)
# iss me hua kya ye pehele A me gya aur phir leke aaya aur phir iss ko super mila to iss ne uss ko bhi change kr diya .. 
print(b.Special, b.classvar1, b.var1)

