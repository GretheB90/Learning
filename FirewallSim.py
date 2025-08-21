import random #To generate random IP addresses

#Generates a random IP for out script:
def generate_random_ip(): #Defining the generate_random_ip function.
    #Generate random numbers for the 3rd and 4th parts of the IP:
    part3 = random.randint(0, 255)
    part4 = random.randint(0, 255)
    return f"192.168.{part3}.{part4}" #Going to return value.

#Check if IP is in the block list or not:
def check_firewall_rules(ip, rules): #recieves IP and rules argument.
    for rule_ip, action in rules.items(): #Using a for loop to unpack the dictionary, using the items function.
        if ip == rule_ip: #It will compare the randomly generated IPs with the ones on our Block list.
            return action #Found it in the block list, so block
    return "allow" #If a random generated IP doesn't match the ones in the block list, it will be allowed.

#Defines firewall rules with predefined rules were we match the IP we wish to block and the action we wish to take
def main():
    #List of blocked IPs:
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    } #represented by dictionary with key value representing the IP addresses as well as the action taken.
    
#Simulates Network traffic by generating 12 random IP addresses and checking them against the firewall rules. Prints us the results.  
    for _ in range(12): #declaring a for loop that will run 12 times. (Simulates network traffic)
        ip_address = generate_random_ip() #Creating a variable. Assigned the value returned by the generate random ip function.
        action = check_firewall_rules(ip_address, firewall_rules) #Creating a variable.
        random_number = random.randint(0,9999) #Creating a variable. Functions as a unique identifier
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

#Ensures that the main function runs once the script is executed.
if __name__ == "__main__":
    main()
