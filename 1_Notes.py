# agr aapne ko kuch aaisa hona jo kuch bhi na like to pass likhna hota hai to vo error throw nhi krta..


# ---------------------------------------pass---------------------------------------------

# ___________________________________VERY VERY IMPORTANT________________________________________

# class Saransh:
#     Chutti = 3

# Chickoo = Saransh()
# Shashwat = Saransh()

# Chickoo.Name = "gandu  "
# Chickoo.Age =8

# Shashwat.Name = "Shashwat Agrawal"
# Shashwat.Age = 15

# print(Chickoo.Age)
# print(Chickoo.Chutti)
# Chickoo.Chutti = 9999
# print(Chickoo.Chutti)
# print(Chickoo.__dict__)


# I THINK THAT SELF IS TAKEN AS A FIRST AURGUMENT ..
# class Saransh:
#     def details(self):
#         return f"Name is :{self.Name}, Age is :{self.Age}"

# Chickoo = Saransh()
# Shashwat = Saransh()

# Chickoo.Age = 8
# Chickoo.Name = "chickoo"


# AGR AAPNE KO DIRECT AURGUMENT ME DALNA HAI TO AAPAN NHI DAL SKTE HAI JAISE KI ISS ME DALA HAI TO YE ERROR THROW KRDENGA .. JAISE KI AAISA..{{{TypeError: Saransh() takes no arguments }}}AGR AAPAN NE DIRECT DALNE KI KOSISH KI TO .. {{{Chickoo = Saransh("SARANSH", 8)}}} TO USS KE LYE EK INTI FUCNTION HOTA HAI VO LAGANA HOTA HAI TO HI KAM KRENGA YE .. 

# class Saransh:
#     def details(self):
#         return f"Name is :{self.Name}, Age is :{self.Age}"

# Chickoo = Saransh("SARANSH", 8)
# Shashwat = Saransh()


# ___________________________--------------CONSTRUCTORS------------------___________________________

# class Saransh:
#     No_of_leaves = 33
#     def __init__(self, Name, Salray, Role):
#         self.name = Name
#         self.salary = Salray
#         self.role = Role


#     def details(self):
#        return f"Name of saransh is :{self.name}, Age of saransh is :{self.salary}, Role of saransh is :{self.role}"

# Shashwat = Saransh("gandu ", 30, "gandu Saf kr ne wala ")

# print(Shashwat.salary)
# print(Shashwat.details())


# def fourthpower(a):
#     return a*a*a*a
# func = [fourthpower]
# for i in range(101):
#     val = list(map(lambda x:x(i), func))
#     print(val)

