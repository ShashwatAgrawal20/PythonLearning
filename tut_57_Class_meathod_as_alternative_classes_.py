# -------------------------------------VERY VERY IMPORTANT--------------------------------------------
#  CLASS MEATHDO..

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


shashwat = Employee("shashwat", 100000, "School")
chickoo = Employee("chickoo", 303, "goo khana")

shweta =Employee.from_str("shweta-33-kuch bhi nhi krti hai ")

print(shweta.salary)
print(shweta.name)
print(shashwat._no_of_holidays)
print(shweta._no_of_holidays)
shweta.change_leaves(33)
print(shweta._no_of_holidays)
# print(shashwat.salary) 
# print(shashwat.printdetail())
# print(shashwat._no_of_holidays)
# (shashwat.change_leaves )= (33,34)
# print(shashwat._no_of_holidays)