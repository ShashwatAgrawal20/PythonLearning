# This is a very very important thing don't ignore it .. very very important !!!!!!!!!!

import time 
from functools import lru_cache

# @lru_cache(maxsize=3)
# def hello (n):
#     # Any task taking n second .. 
#     time.sleep(n)
#     return n

# # iss ko aapan variable me store kr ke bhi kr skte hai ye funciton agr aapan ne 10 bar call kiya to to yye 30 second lagayange.. iss lye iss ko aapan function caching krvate hai ye bhi bhot kam ka hai .. iss ko aapan aaisa bolte hai ki aabhi store kr le bad me jab bhi call honga tabhi tune  bilkul bhi time mtlagana .. kuch iss prakar ka hihota hai ye .. agr nhi smj me aaya to(https://www.youtube.com/watch?v=34p5CH48hLE&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=76&ab_channel=CodeWithHarry)


# # ye joi hai ye latest 3 ya jobhi aapan ne maxsize me dali hai utne ko hi store kr enga.. ye bhi kam ka hai bhot .. 
# if __name__ == "__main__":
#     print("Now using hello")
#     hello(3)
#     print("Shashwat is a good boy")
#     hello(3)
#     print("calling the function again")
#     hello(3)
#     print("The function ended")



# agr aapan ne kuch iss prakar kiya to ye dono taraf time lenga kyuki iss me iss ne max widht set kr li mtlb vo jada se jada itene hi store kr skta hai . to iss lye vo time lenga.. 


@lru_cache(maxsize=34)
def hello (n):
    # Any task taking n second .. 
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("Now using hello")
    hello(3)
    hello(3)
    hello(2)
    hello(3)
    print("Shashwat is a good boy")
    hello(3)
    print("calling the function again")
    hello(3)
    print("The function ended")