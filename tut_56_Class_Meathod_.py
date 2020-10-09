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
    #iss se ye class mme ka hi change krdetta hai kyuki ye class variable hai 
    def change_leaves (cls, leaves):
        cls._no_of_holidays=leaves

shashwat = Employee("shashwat", 100000, "School")
chickoo = Employee("chickoo", 303, "goo khana")

print(shashwat.salary) 
print(shashwat.printdetail())
print(shashwat._no_of_holidays)
chickoo.change_leaves(33)
print(chickoo._no_of_holidays)
print(Employee._no_of_holidays)