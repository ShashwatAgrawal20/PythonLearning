# Important and Very easy

# kisi chij ke bare me pta krna jaise str ek object hai aur int bhi ek object hai kisi object ke barae me mahiti nikalna hai ki vo kha se aaya hai konse class se aaya hai .. vo ye pta kr ke deta hai object introspection

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

Shashwat = Employee("Shashwat", "Agrawal")
Saransh = Employee("saransh", "gandu")
# print(Shashwat.email)
# ye jo type hai ye ek introspection hai 
print(type(Shashwat))
print(type("Shashwat"))
# ye jo hai ye id bhi har object ki alg alg hoti hai har ek object ki jee haa.. ye jo hai ye har bar run kr ne pr change hoti hai aur ye jo hai ye niche wale iss me iss kye lye nhi hui hai kyuki vo jo hai vo ek hi nam ke hai agr aapan ne ek letter bhi change kr diya to ye backened me alg nam se save hua hai agr ek space bar bhi de diya to bhi change ho jayenga..ye  
# print(id("hello"))
# print(id("hello "))

# ye aapne ko vo sari chije de dengea jo aapan iss ke andr kr skte hai jaise ye iss ke aapan ye kr skte hai  ye jo hai ye dikhata hai ki isss se aapan kya kya khilwad kr skte hai 
o = "This is a String"
# print(dir(o))
# print(dir(Shashwat))



# iss me jo hai ek inspect module hota hai 
# to ye vo sb chije return kr denga ki aapne pass kya kya hai iss me jasie ye jo hai iss se anaeder ek deleterattribute hai vge re vgere hai vo sb ye dikhata hai 
# ye getmember ek function hai 
import inspect
print(inspect.getmembers(Shashwat))