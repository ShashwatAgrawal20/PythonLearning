# We have to search the Built in Exception in Python

# s = input("What is your name \n")


# if s.isnumeric():
#     raise Exception("Numbers are not allowed ")
# print(f"Hello {s} ")


# Kuch iss prakar se bhi aapan iss ko use kr skte hai .. bhot kam ka hai ye bhot sare hote hai iss me vo khud se explore krne hai 


# a = int(input("Enter the First Number"))
# b = int(input("Enter the Second Number"))


# if b == 0:
#     raise ZeroDivisionError("The input of b is zero")


# def hello (a, b):
#     if b == 0:
#         raise ZeroDivisionError("The input is 0")
#     return (a/b)
# a = hello(3, 0)
# print(a)


# iss se ye jo niche wala hai ye iss me ye ek sath 2-2 error aagye hai ek vo a wala hai aur ek jo hai vo manually generated hai .. 


c = input("Enter your Name\n")
try:
    print(a)
except Exception as e:
    if c == "Shashwat":
        raise ValueError("Your are not allowed")

    print("Ye jo print statement hai ye Exception handeling ke lye hai")
