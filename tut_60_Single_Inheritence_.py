# class ko ek dam copy krke uss me dusri chije add krna .. 
# Single inheritance

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

class yo (Employee):
    no_of_leaves = 343
    def __init__(self, Name, Salary, Role, Languages):
        self.name = Name
        self.salary = Salary
        self.role = Role
        self.languages = Languages
    
    def printprog(self):
        return f" The Name is: {self.name}. Salary is: {self.salary}. Role is: {self.role}.Languages are {self.languages}"



shashwat = Employee("shashwat", 100000, "School")
chickoo = Employee("chickoo", 303, "goo khana")

print(shashwat.__dict__)
shweta = yo("chikan", 33, "gandu", ["python"])
print(shweta.printprog())
print(shweta.no_of_leaves)
