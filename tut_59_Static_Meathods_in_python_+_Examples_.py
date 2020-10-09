# iss ke pehele tak aapan ne dheka apan ne jo aurgument diye vo self me jate the nhi to uss me nhi dalne hai to @classmeathod ka use krna pdta tha uss ke lye  

# lekin agr aapne ko sirf meathod hi lagani hai to vo kaise kre vo  hai iss me .. 

class Employee:

    _no_of_holidays = 8

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

    @staticmethod
    def hello(string):
        print( string+"is a good boy")
        return("ye jo bhi upar ka hai ye zhoot hai ")


shashwat = Employee.from_str("Shashwat-33000000-Kuch bhi nhi ")
# iss me none iss lye aaya kyuki aapan ne kuch return hi nhi kiya
saransh = Employee("Gandu", 3000000000, "Gandu Chale")
# print(shashwat.)
print(shashwat.hello("chikan seth bhot aache bacche hai ek no ke aache kam krne wale hai vo insann"))