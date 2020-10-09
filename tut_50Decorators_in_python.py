# def function1():
#     print("chikan tatti hai..")
# func2 = function1
# del function1
# func2()

# -------------------------------------------MAKING FUNCITON IN FUNCTION.---------------------------------------------


# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum

# a = funcret(1)
# print(a)
# apan ek funciton ko function se bhi return krskte hai .. 

# aapan niche ke jaise function ke andar function bhi dal skte hai .. jaise niche dala hai aur uss me aurgument bhi dal skte hai 

# def executor (func):
#     func("this")
# executor(print)



# -------------------------------------------DECORATORS----------------------------------------------

# def dec1(function1):
#     def nowexec():
#         print("exciting now")
#         function1()
#         print("excuted")
#     return nowexec
# def who_is_shashwat ():
#     print("shashwat is a good boy")
# who_is_shashwat = dec1(who_is_shashwat)   
# who_is_shashwat()


# iss ko likhne ka ek aur aasan tarika hai ------------who_is_shashwat = dec1(who_is_shashwat)  --------------------

# ye bhi aaise hi kam krta hai bas @dec1 lagana honga.. 
def dec1(function1):
    def nowexec():
        print("exciting now")
        function1()
        print("excuted")
    return nowexec

@dec1

def who_is_shashwat ():
    print("shashwat is a good boy")   
who_is_shashwat()



# --------------------------------------DECORATORS SAMAPT-----------------------------