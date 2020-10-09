# try:
#     f = open("halkat.txt")
# except Exception as e:
#     print(e)
# finally:
#  print("shashwat is a good boy")


try:
    f = open("shashwat.txt", "r")
except Exception as e:
    print(e)

except EOFError as e:
    print("An EOF error occurs", e)

except IOError as e:
    print("An EOF error occurs", e)
else:
    print("hello ")
finally:
    print(f.readlines())
    f.close()
