# -----------------------Aapan ye koi bhi nam se bna skte hai ye 3variables-----------------------------------------

# public - jo aapan sb ke samne revel krna chate hai .. jaise ki {{no_of_leaves = 343}}


# protected - jo aapan aapne ghar walo ko dikhana chate hai{object oriented ke iss me mtlb hota hai ki jo class hai vo to iss ko use krhi skti hai iss ke alava jis se ye derive hue hai vo bhi use kr skte hai lekin ye variable banane ke lyeaapna ko starting me _aur variable ka nam likhna hota hai }


# private - jo aapan kis ko bhi nhi batana chate hai vo hota hai private variable{ye jo private variable banane ke lye aapne ko __ aur phir variable ka nam likhna hota hai .. ye bhi kam ka hai bhot .. ye aapan jaise dusre acess krte hai vaise nhi krskte hai jaise.. ki{print(shashwat._shashwat)} }

class Employee:

    _no_of_holidays = 8
    _shashwat = 34
    __chikan = 333

    def __init__(self, Name, Salary, Role):
        self.name = Name
        self.salary = Salary
        self.role = Role

    def printdetail(self):
        return f" The Name is: {self.name}. Salary is: {self.salary}. Role is: {self.role}"

    @classmethod
    def change_leaves (cls, leaves):
        cls._no_of_holidays=leaves
    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
# iss ka ek one liner bhi hai aapan agrs aur kwargs bhi use krskte hai yha pr .. ye bhi kam ka hai .. 
        return cls(*string.split("-"))

class yo (Employee):
    no_of_leaves = 343
    def __init__(self, Name, Salary, Role, Languages):
        self.name = Name
        self.salary = Salary
        self.role = Role
        self.languages = Languages
    
    def printprog(self):
        return f" The Name is: {self.name}. Salary is: {self.salary}. Role is: {self.role}.Languages are {self.languages}"

shashwat = Employee("shashwat", 300000, "Ek no ka baccha hai ye")        
print(shashwat._shashwat)
# ye jo niche wala hai iss ko aapan aaise acess nhi krskte hai ye error throw krdenga.. agr acess krna hai to ._class ka nam bhi dalna hota hai aur phir jo hai vo aata hai private variable.. yha pr python nameangling krdeti hai vo hota to hai lekin python uss ka nam kuch iss tarah save krti hai iss lye kyuki aapan vo galti se bhar use na krde.. {{print(shashwat._Employee__chikan)}} yha pr class Employee thi iss lye vo likha hai .. 
# print(shashwat.__chikan)
print(shashwat._Employee__chikan)