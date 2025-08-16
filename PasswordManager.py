import bcrypt #Helps us lock (encrypt) passwords so others can't read them.
import getpass #Lets you type your password without anyone seeing it on the screen.
import string #Gives us a list of characters, like letters, numbers, and symbols.

password_manager = {} #This is like our locker database

def check_password_strength(password): #This is a function. Think of it as a mini program that runs when we want to judge a password
    has_upper = any(c.isupper() for c in password) #Does it have big letters? (A, B, C). Look at each letter (c) in the password.
    has_lower = any(c.islower() for c in password) #Does it have small letters? (a, b, c)
    has_digit = any(c.isdigit() for c in password) #Does it have numbers? (1, 2, 3)
    has_symbol = any(c in string.punctuation for c in password) #Does it have symbols? (@, #, $)
    is_long = len(password) >= 8 #Is it at least 8 characters?

    score = sum([has_upper, has_lower, has_digit, has_symbol, is_long])

    if score == 5:
        return "Strong!"
    elif score >= 3:
        return "Medium~"
    else:
        return "Weak..."

def create_account():
    username = input("Enter a username: ").strip() #Asks for a username
    if username in password_manager: #Checks if that username already exists
        print("That username already exsist! try logging in.")
        return
    
    password = getpass.getpass("Enter a password: ").strip()
    strength = check_password_strength(password) #Checks the password strength
    print(f"Password Strength: {strength}")
    
    if strength == "Weak...": #Rejects if it’s Weak:
        print("Password is too weak! Please use a mix of uppercase, lowercase, numbers, symbols, and at least 8 characters.")
        return
    
    #Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) #Scrambles (encrypts) the password using bcrypt:
    password_manager[username] = hashed_password #Saves the account
    print("Account created successfully!")

def login():
    username = input("Enter your username: ").strip() #Asks for username
    password = getpass.getpass("Enter your password: ").strip() #Asks for password

    if username in password_manager: #Checks if the username is in the database
        stored_hash = password_manager[username]
        if bcrypt.checkpw(password.encode(), stored_hash):
            print("Login Successful!")
        else:
            print("Login failed! Invalid password.")
    else:
        print("Login failed! Username does not exist.")

def main(): #This is like the main loop of a game. Keeps running until you say “I’m done.”
    while True:
        choice = input("\nEnter 1 to create an account, 2 to login, or 0 to exit: ").strip()
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0": #It repeats forever until you press 0
            break
        else:
            print("Invalid choice.")
        
if __name__ == "__main__": #“If you run this file, start with the main() function.”
    main()
