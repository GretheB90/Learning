import random #Gives the ability to create a random output given inputs
import string #Adds to the string compability

#The password making machine:
def generate_password(length: int = 10):
    #Remove tricky characters like quotes and backslashes
    unsafe_chars = "\"'\\`"
    safe_punctuation = ''.join(c for c in string.punctuation if c not in unsafe_chars)
    
    #Build the character pool
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    #Generate the password
    password = "".join(random.choice(alphabet) for i in range(length)) #Pick something from a "box" until we have the amount we ask for and stick them together
    return password

def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    is_long = len(password) >= 8

    score = sum([has_upper, has_lower, has_digit, has_symbol, is_long])
    
    if score == 5:
        return "Strong!"
    elif score >= 3:
        return "Medium~"
    else:
        return "Weak..."
    
# Main program
if __name__ == "__main__":
    try:
        user_input = input("How long should the password be? (default is 10): ").strip()
        user_length = int(user_input) if user_input else 10

        password = generate_password(user_length)
        strength = check_password_strength(password)

        print(f"\nGenerated Password: {password}")
        print(f"Password Strength: {strength}")

    except ValueError:
        print("Please enter a valid number.")

#Ask the user how long the password should be:
#try:
    #user_length = int(input("How long should the password be? (default is 10): ") or 10)
    #password = generate_password(user_length)
    #print(f"Generated password: {password}")
#except ValueError:
    #print("Please enter a valid number.")

#password = generate_password()
#print(f"generated password: {password}")
