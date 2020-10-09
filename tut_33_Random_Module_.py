import random
# ye random.randint iss se aapan vo list me se koi bhi kr skte hai 
random_number = random.randint(0, 5)
# iss se apne ko jo bhi apan ne dye hai jaise aapan ne diya hai 0 to 5 to ye 0 se 5 ke bich me koi bhi number de skta hai vo repeat bhi ho skte hai 
print(random_number)
rand=random.random() *100
# ye sirf 0 se lekar 1 tak hi print krenga aur ye float value denga jo decimal me hoti hai vo wali agr aapan ko dusre tak krwane hai to * jo number honga vo likh dena ho  jayenga jaise aapan ne upar *100 kiya hai to ye 0 se lekar 100 tak ke print krenga aur float me krenga.. ye numbers hai 
print(rand)

# ek hota hai random.choice
lst=[
    "StarPlus", "DD1", "Aaj Tak", "CodeWithHarry"
]
choice = random.choice(lst)
# iss se aapan koi bhi iss koi bhi iss ko means string ko use krskte hai jaisse alag alag nam de diye aur aur ye funciton laga diya to ye aapne ko random denga 
print(choice)


# aapne ko iss ke aage koi bhi do module le ke uss ke do do function likhne hai.. 




