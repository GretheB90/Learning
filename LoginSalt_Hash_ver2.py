import bcrypt

#----- SIGNUP (Create new user and store password securely) -----

def hash_password(password):
    #Generate a salt and hash the password (bcrypt includes the salt inside the hash)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed  #Already includes salt

# Simulating signup
user_password = input("Create a password: ")
hashed_password = hash_password(user_password)

# Fake database (just for simulation)
user_db = {
    "username": "Alice",
    "hashed_password": hashed_password  # store the full hash (includes salt)
}

print("Password securely stored for user Alice.\n")

#----- LOGIN (Verify password entered by the user) -----

def verify_password(input_password, stored_hash):
    return bcrypt.checkpw(input_password.encode(), stored_hash)

# Simulating login
input_password = input("Enter your password to log in: ")
is_valid = verify_password(input_password, user_db["hashed_password"])

if is_valid:
    print("Login successful! Welcome, Alice.")
else:
    print("Wrong password! Access denied.")
    
#Why is this code better than ver1?
#Old: used SHA.256. New: using bcrypt for better safety.
#Old: Stored salt seperately. New: Salt is now included in the hash.
#Old: Fast, but weak. New: Intentionally slower = more secure.
#Old: Manual checking. New: Uses bcrypt.checkpw()
