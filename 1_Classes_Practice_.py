class form:

    no_of_leaves = 33

    def __init__(self, Name, Salary, Occupation):
        self.name = Name 
        self.salary = Salary
        self.occupation = Occupation

    def details(self):
        return f"Name is {self.name}, Salary is {self.salary}, Occupation is{self.occupation}"

    @classmethod
    def change_leaves (cls, leaves):
        cls.no_of_leaves = leaves
    @classmethod
    def gandu (cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

# ye jo aapan ne init ka function banaya hai ye bhi kam krta hai iss me bas value dal do tho bhi kam krrha hai ye .. 
shashwat = form("shashwat", 333, "kam dhande krne wala manushya.. ")
saransh = form("gandu ", 30, "gandu chale")
anekar = form.gandu ("Timepass")
# shashwat.name= "shashwat"
# print(shashwat.name)
print(shashwat.name)
# print(shashwat.details())
print(saransh.name)
# print(saransh.details())
print(shashwat.no_of_leaves)
form.no_of_leaves = 333
print(shashwat.no_of_leaves)
# ye aapan bar bar no of leaves change krne se aacha hai upar ke jaisa funciton bana le aur phir uss ko aaisa jaisa niche diya hai vaise change kre to ek no mja aajati hai .. bhot kam me bhi aata hai ye kam ka bhi hai ye bhot ye hi use krna hai vo purani meathod use nhi krni hia aabhi to bhi.. 
shashwat.change_leaves(33333)
print(shashwat.no_of_leaves)

print(anekar.occupation)
