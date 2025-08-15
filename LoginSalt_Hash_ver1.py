#--Signup(Storing a new password):--#

import hashlib #helps turn the password into a secret code (hash)
import os #helps make a random "salt"

def hash_password(password):
    salt = os.urandom(16) #generate 16-byte salt
    combined = password.encode() + salt
    hashed = hashlib.sha256(combined).hexdigest()
    return salt.hex(), hashed

#--Simulating signup:--#

#New user signup
user_password = input('Password: ')
salt, hashed_password = hash_password(user_password)

#Save both in database (simulate with dictionary)
user_db = {
    "username": "Alice",
    "salt": salt,
    "hashed_password": hashed_password
}

#--Login(Verifying a Password):--#

def verifying_password(input_password, stored_salt, stored_hash):
    salt_bytes = bytes.fromhex(stored_salt)
    combined = input_password.encode() + salt_bytes
    input_hash = hashlib.sha256(combined).hexdigest()
    return input_hash == stored_hash

#Simulate login:

input_password = "password123"
is_valid = verifying_password(input_password, user_db["salt"], user_db["hashed_password"])

print("Login Successful?" , is_valid)

#If the password matches, it will print:
#Login successful? True

#In real life, using sha.256 is risky, use other alternatives instead like bcrypt.
