import random

def homepage():
    print("""  
    Number Guessing Game
    
    Pick a number 1 to 3
    """)

score = 0
attemp = 3
    
homepage()            
while attemp > 0:
    user_choice = int(input("Number: "))
    
    computer_choice = random.randint(1, 3)
   
    print(f"Computer choice: {computer_choice} User's choice: {user_choice}\n")
    print(f"You have {attemp} attemp left")
    
    if user_choice == computer_choice:
        print("You guessed me \n")
        score += 1
    else:
        print("You guessed it wrong \n")
        attemp -= 1
    
print(f"Your score: {score}")