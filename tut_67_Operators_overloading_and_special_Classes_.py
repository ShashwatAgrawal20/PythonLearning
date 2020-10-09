# we have to search mapping operators to functions..////////////////////// ye search kr na hai to iss ka pura page mil jayenga .. bhot imp hai ye 

class Employee:

    _no_of_holidays = 8

    def __init__(self, Name, Salary, Role):
        self.name = Name
        self.salary = Salary
        self.role = Role

    def printdetail(self):
        return f" The Name is: {self.name}. Salary is: {self.salary}. Role is: {self.role}"

    # @classmethod
    # #iss se ye class mme ka hi change krdetta hai kyuki ye class variable hai 
    # def change_leaves (cls, leaves):
    #     cls._no_of_holidays=leaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary
    
    def __repr__(self):
        # return f" The Name is: {self.name}. Salary is: {self.salary}. Role is: {self.role}"
        return f"Employee {self.name}, {self.salary}, {self.role}"

# agr str funciton hai to ye pehele str ko print kr na preffer kr tha hai jab bhi agr repr hai to bhi ye str likhna prefer kr ta hai .. iss ko aapan jab tak uss ko praticular nam lekar nhi likhte hai tab tak vo repr hai vo run nhi hota hai ..print(repr(emp))  Aapne ko repr lena hai to ye aaise likhna hota hai .. bhot kam ka hai ye functions...
    def __str__(self):
        return f" The Name is: {self.name}. Salary is: {self.salary}. Role is: {self.role}"


emp = Employee("Shashwat", 3434, "School")
emp2 = Employee("Saransh", 34, "Gandu")

# do object ko jod ne ke lye dandar meathod lagana hota hai .. 
print(emp+emp2)
print(emp/emp2)
print(emp)

print(repr(emp))