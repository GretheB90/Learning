#Is a Query and Response protocol. Is used for querying large publicly available databases and these contains info of registered users. (Domain names and IP addresses)

import socket #Let's Python talk to other computers.

def whois_lookup(domain: str):
    s = socket.socket(socket.AF_INET, #setting a variable called s, creating a socket using the socket method. Socket 1/AF_INET(address family internet socket)
    #I want to talk over the internet using IPv4 addresses.
    socket.SOCK_STREAM) #Socket 2 also called Socket stream. Declaring that we want a TCP socket type as we're making a TCP request, using the whois function.
    #“I want a reliable phone call — like talking on a phone where the message gets delivered perfectly in order.”
    s.connect(("whois.iana.org", 43)) #Using the connect function from socket library, connecting to the URL.
    s.send(f"{domain}\r\n".encode()) #Sends a request/query to the domain which define later. Gonna define it as a byte of strings moving.
    #You say the domain name (like "google.com") followed by special characters (\r\n) which mean “end of message” — like saying “Over!” on a radio
    #The .encode() changes your words into a secret code(bytes) that computers can read.
    response = s.recv(4096).decode() #Responsible for receiving a response from the whois server and going to give it a buffer of 4096 and it will decode it into strings for readability.
    s.close() #closing the socket/Call.
    return response #returning the response

# Example usage
print(whois_lookup("google.com")) #calls the whois_lookup function. Takes the argument, google.com and prints a response.

#SOCK_STREAM = Like a phone call
#SOCK_DGRAM = Like sending a postcard or a quick message
#AF_INET = "Talk over the internet"
#Connect to whois.iana.org on port 43 (the whois hotline)
