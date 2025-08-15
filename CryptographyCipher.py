import string  #Makes Strings a bit more flexible/improved. Allows for more complexity (knows all lowercase letters).

def caesar_encrypt(message, key):   #Starts with two variables. Message is the thing we want to encrypt. Key is the number of positions to shift down the alphabet to create the encrypted message.
                                    #Creates a translation table for the Cipher 
    shift = key % 26 #Making sure the key is always between 0 and 25 due to the amount of letters in the alphabet. 
    #cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    
    #Create translation tables for lowercase and uppercase
    lower_original = string.ascii_lowercase
    lower_shifted = lower_original[shift:] + lower_original[:shift]

    upper_original = string.ascii_uppercase
    upper_shifted = upper_original[shift:] + upper_original[:shift]

    #Combine both into one big translation table
    cipher = str.maketrans(lower_original + upper_original,
                           lower_shifted + upper_shifted)

    encrypted_message = message.translate(cipher)  #No more .lower()!

    #encrypted_message = message.lower().translate(cipher) #Translate method to encrypt the message. Shifts each individual character 3 to the right down the alphabet to get encrypted message.

    return encrypted_message


def caesar_decrypt(encrypted_message, key): #We need the encrypted message and we need the key again so that encrypted message is a variable we put in the first function.
                                            #Function will again create a translation table for the cipher    
    shift = 26 - (key % 26)
    #cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    
    lower_original = string.ascii_lowercase
    lower_shifted = lower_original[shift:] + lower_original[:shift]

    upper_original = string.ascii_uppercase
    upper_shifted = upper_original[shift:] + upper_original[:shift]

    cipher = str.maketrans(lower_original + upper_original,
                           lower_shifted + upper_shifted)

    message = encrypted_message.translate(cipher) #This time it translates in reverse
    return message 

message = "Subscribe to my newsletter"  #The variables we used in both the above functions. This is a string.
key = 3                                 #This is a integer and is how many layers we want to shift down the alphabet to create encrypted message.

encrypted_message = caesar_encrypt(message, key) #Setting a variable called encrypted message which calls for the caesar_encrypt function with the message and key variables as arguments
print(f"Encrypted message: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"decrypted message: {decrypted_message}")
