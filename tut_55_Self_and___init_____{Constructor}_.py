# -------------------------------------VERY VERY IMPORTANT--------------------------------------------
# Meathod
# convectioon of object oriented programming .. iss me as an argument jis pr lagaya ye funciton vo jayenga.. jaise rohan pr lagane ke lye.. print(chickoo.printdetail()) aur vaise hi mere iss pr lagane ke lye .. print(shashwat.printdetail())

# iss me self as a first aurgument lagta hai.. self first meathod hota hai .. 
class Employee:
    _no_of_holidays = 8

    def __init__(self, Name, Salary, Role):
        self.name = Name
        self.salary = Salary
        self.role = Role
    def printdetail(self):
        return f" The Name is: {self.name}. Salary is: {self.salary}. Role is: {self.role}"

shashwat = Employee("shashwat", 100000, "School") # ye jo aurgument jo hai ye hamesha __init__ ko hi jate hai . ye bhot main bat hai . 

# chickoo = Employee()

# shashwat.name = "Shashwat"
# shashwat.salary = 500
# shashwat.role = "Go to School"

# chickoo.name = "Saransh"
# chickoo.salary = 100
# chickoo.role = "gandu"

# print(chickoo.printdetail())
# print(shashwat.printdetail())

# print(chickoo._no_of_holidays)

# ------------------------------------- CONSTRUCTOR--------------------------------------------------

# THE WAY OF GIVING THE AURGUMENT TO A CLASS IS CALLED AS CONSTRUCTOR.. BUT WE HAVE TO MAKE THE __INTI__FUNCTION FOR IT.. 

# INIT FUNCITON RUNS AUTOMATICALLY..

print(shashwat.salary) 
print(shashwat.printdetail())