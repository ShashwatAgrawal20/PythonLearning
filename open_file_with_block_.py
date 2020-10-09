with open ("shashwat.txt", "r+") as f:   #iss me aapen ko close kr ne ki zhanzat nhi reheti hai
    f.write("chickoo gandu hai \n")
    print(f.read())

# agr aapan ne ye niche wala with block ke bhar nikal ke phri se likha to bhi ye print honga

f = open("shashwat.txt", "r+")
print(f.read())
f.close()
