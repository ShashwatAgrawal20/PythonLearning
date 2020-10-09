# f = open("shashwat.txt", "w")   # agr aapne ko write krna hai to aapne ko ye w mode me kholna pdta hai ....
# f.write("i am a good boy")      # iss me aapen ko bas pointer likhke aapne ko bas run krna hai aur ye ho jayenga

# f.close()

# f = open ("shashwat.txt", "a")
# f.write("chickoo gandu hai \n")
# # iss ko aapan jitne bar run krenge utne bar ye vo content uss me paste krenga...
# # aur agr aapan ne iss ko write mode me khola to ye aapne ko vo content ko remove kr ke ye content denga
# f.close()

# f = open ("shashwat.txt", "w")
# f.write("chickoo seth gandu hai .. ")    # ye hai write mode iss me ek aur mode hota hai read and write both 
# f.close()


f = open("shashwat.txt", "r+")
a = f.read()
f.write("chickoo seth halkat hai gandu hai ")
print(a)
f.close()


