# ---------------------------------VERY VERY IMPORTANT WRITING OUR FIRST CLASS----------------------

class Employee:
    # ye sb ke lye same honge jitne bhi aapan ne object banaye hai jaise shashwat ko bhi ye hi class di hai .. to ye uss me bhi rhega aru chickoo me bhi honga.. aur agr print kra to ho bhi jayenga
    _no_of_holidays = 150
    pass

shashwat = Employee()
chickoo = Employee()

shashwat.name = "Shashwat"
shashwat.salary = 500
shashwat.role = "School"

chickoo.name = "Saransh"
chickoo.salary = 100
chickoo.role = "gandu"

# ye jo shashwat ki salary hai ye iss ki khud ki property hai iss me class ka kuch bhi nhi hai role.. 
print(shashwat.salary)
print(shashwat._no_of_holidays) # ye aapan ne class me diya hai iss me particular me nhi diya hai . direct class me hai .. 
# aapan iss ko kis se bhi acess kr skte hai jaise
print(chickoo._no_of_holidays)
print(Employee._no_of_holidays)

# leikin agr iss ko change kr na hai to ye class se hi honga jo ki iss me hai Employee .. 
# agr aapan ne iss ko prticular name se kiya to ye sirf uss ke lye honga. mtlb instance me aajayega vo jaise;;;;;;shashwat._no_of_holidays = 33409
print(shashwat.__dict__)
Employee._no_of_holidays = 200 
print(shashwat._no_of_holidays)
shashwat._no_of_holidays = 33409
print(shashwat.__dict__)
print(chickoo._no_of_holidays)
Employee._no_of_holidays = 200
print(Employee.__dict__)
# ye jo dict hai ye fucntion ek dictionary return krta hai uss me pta chalta hai kon kon si classes hai vge re..