i = 18
print("This is a guess the number game..\n")
number_of_guesses = 1

print("you have 9 number of guesses.. \n")


while(number_of_guesses<=9):
    guess_number = int(input("Guess the number\n"))
   
    if guess_number>18:
        print("you entered  high number")
    elif guess_number<18:
        print("you entered too small number")    
    else:
        print("you won the game ")    
       
        break
    print(9-number_of_guesses, "Moves left")
    number_of_guesses = number_of_guesses+1





 
   
   
