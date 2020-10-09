
# iss me aapna program ko exit hone se bcha skte hai ....


print ("Enter the num 1")
num1 = input()
print("Enter the num 2")
num2 = input()

try:
    print("The sum of two numbers are",   # ye bs try krenga aur agr run ho gya to phir properly run ho jayenga aur ,
                                          # agr nhi hua to phri ye line ko bhula ke agla code execute krne lgenga ......
    int (num1)+int (num2))

except Exception as e:
    print (e)

print("This line are very important ...")


d1={"hi":"hello", "matti":"tatti", "halkat":"khora "}
n=input()
try:
    print ("word is ", (d1[n]))
except Exception as e:
    print("No word found you entered :",e)
   
      