# ye jo hai ye pehele write ho jata hai aur phir bad me change bhi kiya to bhi nhi hota hai kyuki iss me pehele se hi ye init ne ye le liya  hai to ye resolve to honga mgr change nhi honga uss ke lye aapane ko init me se function nikalna honga aur phir uss ke bad jo hai vo email me dalna honga.. to ye kam kr jayenga aur iss ko bolte hai setter property.. ye kyu hua ki ye aapan ne init ko nikal diya hai .. agr aapne ko kuch iss prakar kr na hai ki vo jo hai uss me aapane ko as a function run nhi kr na hai sadhe ke jaisa hi run kr na hai to uss ke lye ek @property decorator hota hai vo bhot kam ka hota hai uss se johai vo function run kr ne ke lye paranthesis nhi lagane honge bhot hi jada useful hai ye .. 
# agr aapan ne ye lagaya to ye aapane ko dikhayaenga ki str object is not callable . 

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"


    def explain(self):
        return f"This is Employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.lname == None or self.fname == None:
            return("Email is not set please set it using setter") 
        return f"{self.fname}.{self.lname}@gmail.com"


    # agr aapne ko kuch iss prakar hona ki aapan ek email ko input de aur vo uss pr se fname aur lname decide kre to aapne ko kya kr na honga.. Shashwat.email="erer.erjkej" agr kuch aaisa diya to ye error throw kr denga.. 

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.lname = None 
        self.fname = None
        # lekin agr ye lagaya to ye none.none@gmail.com aayenga.. 


Shashwat = Employee("Shashwat", "Agrawal")
Chikan = Employee("Saransh", "Agrawal")

print(Shashwat.email)

Shashwat.fname = "Ram"
print(Shashwat.email)

#ye jo niche ka kaise possibe hua aapan ne iss me jo hai vo setter property lagai hai iss ke lye ye change ho paya hai aaise .. lekin iss ke lye jo hai vo pehel iss nam ka ek function honga chiyea .
Shashwat.email = "erer.ewwerwer@gmail.com"
print(Shashwat.fname)
print(Shashwat.lname)
print(Shashwat.email)

# agar aapen ko koi attribute delete kr na hai to vo aapan aaise hi nhi likh skte hai uss ke lye aapane ko ek deleter bana hota hai 
del Shashwat.email
print(Shashwat.email)

Shashwat.email = "Shashwat.Agrawal@gmail.com"
print(Shashwat.email)