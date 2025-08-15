import bcrypt #Making it harder to break passwords.

#User enters a password
password = input("Enter your password: ").encode()

#Generate salt and hash
salt = bcrypt.gensalt() #This line creates a random salt (just like before with os.urandom, but smarter).
hashed = bcrypt.hashpw(password, salt) #hashpw stands for "hash password". Mixes the encoded password with salt. Scrambles into string called hash.

print("\nYour password has been safely hashed and stored!")
print("Salted and Hashed Password:", hashed.decode())

#To check the password later:

entered = input("\nEnter your password to log in: ").encode()

#Check if the entered password matches the original hash
if bcrypt.checkpw(entered, hashed):
    print("Correct password! Access granted.")
else:
    print("Wrong password! Access denied.")

#Alternatives for sha.256:
#bcrypt
#scrypt
#argon2
