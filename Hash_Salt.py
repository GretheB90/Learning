import hashlib
import os

#User enters a password
password = "password123"

#Generate a random salt
salt = os.urandom(16)   #16 bytes = 128 bits. #os.urandom = cryptographically secure

#Combine and hash
combined = password.encode() + salt
hash_value = hashlib.sha256(combined).hexdigest() # In real code - Use a different hashing algorithm for hasing password (e.g. bcrypt)

print("Salt:", salt.hex())
print("Hashed Password:", hash_value)
