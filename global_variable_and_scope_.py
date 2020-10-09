# l = 10 #Global variable   {ye sarkar ka paisa hai }
# def function1(n):
#     print(n,"I have already printed the number")
#     l = 5  # ye function ki niji sampatti hai agr aapne ko value change hona to aapen ko ek aru variable bananapdenga.. 
#     m = 8
#     print(l, m ) #yha pr bhi ek hi aayegi l ki value ..  
# function1("This is me ")
# print(l)  #agr l ko print kra to aapen ko das milega



# # ye pehele local me dhoondenga aur nhi mila to ye globle me dhoondenga aur uss me bhi nhi mila to error marenga
# l = 10 
# def function1(n):
#     print(n,"I have already printed the number")
#     l = 5  # ye jo l aur m hai ye aapna paisa hai 
#     m = 8  # ye local variale hai .. 
#     print(l, m )   
# function1("This is me ")
# print(l)    # jaise aapne ne yha pr aapne ne global hta diya to ye function ke andar ghoos ke nhi nikal skta hai ye sb 
# # aur vaise hi aapan ne agr m bhi likha to ye error throw krenga.. 



# # Global keywords.. 

# # We cannot change the Global variable {aapna sarkar ki sampatti ko change nhi kr skte hai }
# # aapan iss ko change nhi krskte hai python nhi kr skta hai bina permition se .. 


'''
l = 10 
def function1(n):
    print(n,"I have already printed the number")
    # l = 5  #{agr aapna ne ye hta diya to ye 10 print krnega .. } aur agr aad kr ne ki bat kri to nhi honga kyuki vo global me dhoondenga.. ye iss ko uncomment kra to ye print kr denga vo add ki hui value .. 
    global l   # ye global tab hi kam krenga jab aalpan local variable hataayega aur  iss ke karan uss ko permission mil gai hai value change krne ki aur uss ne change krke print krke dedi hai ..   {ye global keyword hai }
    l = l+45  # ye kra to ye error thorw krenga.. lekin agr aapn ne global l kr diya to iss ko permission mil gai smj lena 
    m = 8  
    print(l, m )   
function1("This is me ")
print(l)'''

# Global variable sidhe bhar jayenga sidhe funciton ke bhar
22
def shashwat():
    x = 20
    def chickoo():
        global x
        x = 89
    chickoo()
    # print("Before calling rohan", x )    
    print("after calling rohan", x)    
shashwat()
print(x)