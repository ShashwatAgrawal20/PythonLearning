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
    var = 500
    no_of_leaves = 343
    def __init__(self, Name, Salary, Role, Languages):
        self.name = Name
        self.salary = Salary
        self.role = Role
        self.languages = Languages
    
    def printprog(self):
        return f" The Name is: {self.name}. Salary is: {self.salary}. Role is: {self.role}.Languages are {self.languages}"

class player:
    var = 400
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printplayer(self):
        return f" The Name is: {self.name}. Game is: {self.game}."   

class lions(Employee, player):
    var = 300
    language = "Python"
    def printlanguages(self):
        return(self.language)


shashwat = Employee("shashwat", 100000, "School")
chickoo = Employee("chickoo", 303, "goo khana")
print(shashwat.__dict__)

go = player("halkat", ['gandu', 'halkat', 'tatti', 'hai', 'sala', 'ek', 'no', 'ka'])
print(go.printplayer())

disco = lions("diwide",34, "kuch bhi nhi ")
print(disco.printlanguages())
print(disco.var)
    
# saurabh = yo("chikan", 33, "gandu", ["python"])
# print(saurabh.printprog())
# print(saurabh.no_of_leaves)