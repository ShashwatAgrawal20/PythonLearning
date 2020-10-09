f = open ("shashwat.txt")   # iss me aapne ko ek dusra aurgument dena pdta hai jo ki aapne konse iss me chiyea vo batata hai..
# jaise ki upar wale iss me maine jaise r likha to ye vaise ka vaise hi print hua hai ... 
# lekin agr maine iss me rb dal diya to ye binary ke iss me aajayenga .
# lekin maine agr iss me r hta diya to ye error phekenga ..
# vo bolega ki kuch na kuch to lagao vo modes jo aapan ne file io basics me lye hai .. 
# content = f.read()
# print (content)

# f.close()

# f = open("shashwat.txt", "rb")
# content = f.read(5555) 
# print("1", content)

# content = f.read(5555) 
# print("2", content)
# f.close()

# we can read  line by line using redline function..

# for line in f:
#     print (line)    # ye tha for loop

# print(f.readline())   # iss se aapan ek line read krskte hai .. readline function se.. ye bhot kam ka hai .. 
# print(f.readline()) 
# print(f.readline())   # agr aapen ye file me jitne hai utne likhne hia 

print(f.readlines())    # iss se aapan ek hi iss me pure iss ko kr skte hai .. ye bhi bhot kam ka hai .. lekin agr aapan ne ye likha to ye \n bhi print krenga jo iss me by default hai .. aur ye ek list ke form me krenga.. ye return.. 
f.close()