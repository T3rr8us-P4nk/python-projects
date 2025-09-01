#Simple Banking management

def homepage():
    print("""
    Banking Management
    
    1. Deposit
    2. Show balance
    3. Exit
    
    """)

balance = 0 
 
 
def show_balance():
    if balance == 0:
        print("You have zero balance")
        add_bal = input("Do you want to add a balance? (Y/N): ")
        
        if add_bal.upper() == "Y":
            deposit()
        elif add_bal.upper() == "N":
            exit()
        else:
            print("Error")
            exit()
    else:
        print(f"Your balance is {balance}")
    
    
def deposit():
    global balance
    amount = int(input("Enter money: "))
    balance += amount
    print("Done")
                                                                                        
homepage()
while True:
    user_input = int(input("Select option: "))
    
    if user_input == 1:
        deposit()
    elif user_input == 2:
        show_balance()
    elif user_input == 3:
        break
        exit()
    else:
        print("Error")