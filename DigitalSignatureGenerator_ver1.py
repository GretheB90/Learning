from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

#Ask the user to type a message:
message = input("Type the message you want to sign: ").encode()

#Generate a private and public RSA key pair:
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

#Sign the message using the private key:
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

#Show the signature (in hexadecimal format for readability):
print("\n Digital Signature (hex):")
print(signature.hex())

#(Optional): Verify the signature:
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    print("\nSignature verified successfully.")
except Exception as e:
    print("\nSignature verification failed.", str(e))
    

#Signs the message using the private key
#Verifies the signature using the public key
