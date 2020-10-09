import time
 
# iss se aapan ye pta lga skte hai ki iss ko run lgne me kitna time lga.. 
initial = time.time()
print(initial)
k = 0
while (k<45):
    time.sleep(2)   
    # ye har do do second bad me print kr ta hai .. jo bhi aapne ko likhana hai apane ko .. ye bhi bhot kam ka hai .. 
    print("Shashwat bhot aacha hai .. ")
    k +=1
print(time.time()-initial)
initial2 = time.time()    
for i in range(45):
    print("Shashwat bhot aacha hai")
print(time.time() - initial2)    


# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)