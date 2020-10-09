'''
i=0
while(i<45):
    print(i+1, end=" ")  # agr aapan ne ye kra to ek sidhe line me sb print ho jayenge.. aur i+1 matlb 1 se chalu honga ...
    i=i+1

i=0
while(True): # while true ek aaisa function hai jo hamesha chalte jayenga kbhi bhi nhi rukenga 
    if i+1<5:
        i=i+1 
        continue   # ye continue function hai ye check kr ta hai ...
    print(i+1, end=" ")  
    if (i==44):
           break#stop the loop(iss ko hi pyar se break bolte hai )
    i=i+1   
'''


#  Quiz hai ye .....................

while (True):
    inp=int(input("Enter a number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Sir please try again")
        continue

    #  iss ki video ek aur bar dekhni pdengi ....

while(True):
    gandu =int (input("Sir please enter a number you want to add : \n"))
    if gandu ==100:
        print("gandu   hai re baba tu pakke me :\n")
        break    
    else:
        print("Halkat chickoo ke jaisa hi rehenga re baba tu :\n")    
        continue


# break and continue bhot kam ki chij hai re baba...