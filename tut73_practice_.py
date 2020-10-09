shashwat = int(input("Enter the number how many times you want to print\n"))
shashwat1 = int(input("Press 1 for list compression \nPress 2 for Dictionary compression\nPress 3 for Set compression\n"))

if shashwat1==1:
    ls = ['This is a List compression'for i in range(shashwat)]
    print(ls)
elif shashwat1==2:
    dc = {i:"This is a Dcitionary compression" for i in range(shashwat)}
    print(dc)
else:
    set = {shashwat for shashwat in["This is a Set compression"]}
    print(set)