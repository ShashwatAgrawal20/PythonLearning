# kabbhi kbhi aapne ko aaisa hona ki thodi chij aabhi hongi aur thodi bad me ya bich me se

# def searcher():
#     import time
#     book  = "Shashwat is a very god boy he is the very good boy"
#     time.sleep(4)


#     while True:
#         # agr aapan aaisa likhte hai ki iss ko ek bracket me likhke yeild kra hai to ye jo funciton hai uss ko ek coroutine ke jaisa leta hai ..
        # text = (yield)
#         if text in book:
#             print("your text is in the book ")
#         else:
#             print("Your text is not in the book ")

# search = searcher()
# print("Search started")
# next(search)
# search.send("Shashwat")
# print("do next thing ")
# input("press any key\n")
# search.send("hoho")
# search.send("ye")
# search.send("good")
# search.send("very")

# search.close()

def search():
    import time 
    # books = ['English', 'Hindi', 'Marathi', 'Maths', 'History', 'Geography', 'Science']
    books = ['English', 'Hindi', 'Science', 'Marathi', 'History']
    time.sleep(2)


    while True:
        text = (yield)

        if text in books:
            print("Yes your search was right")
        else:
            print("Check the spelling or the word!!")

s = search()
next(s)
s.send('English')
s.send('Maths')

