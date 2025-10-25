#This file is excessively commented for my own learning.

#Importing all the required libraries
import os                               #interact with OS
import sys                              #Handles system specific operations(such as exiting the script) 
import time                             #Tracking time intervals (Determine a transfer rate of packets)
from collections import defaultdict     #Used to store and manage packets counts for each IP
from scapy.all import sniff, IP         #Allows to analyze Network packets

#Declare variable representing the threshold for a Dos attack.
THRESHOLD = 40 #Global Variable, represents the maximum Loud pack rate per second for an IP address.
print(f"THRESHOLD: {THRESHOLD}") #Print the threshold values on screen.

#declare a callback function used mainly for incrementing packet counts for each source IP address, calculating the packet rate and blocking the
#IP etherade exceeds the threshold.
def packet_callback(packet):    #Define the packet callbak which recieves the argument packet inside the function.
    src_ip = packet[IP].src     #Inside the function we extract the Source IP address from the packet.
    packet_count[src_ip] += 1   #Increment the packet count for the source IP address.
    current_time = time.time()  #We then record the current time using the time function from the time library.
    time_interval = current_time - start_time[0]  #We calculate the time interval by subtracting the start time from the current time. It's a list containing the start time.
    
    if time_interval >= 1:  #Check if the interval is one, meaning here that the script will evaluate whether or not a Dos attack is happening at the frequency of 1 every second.
                            #If the interval is equal or greater than 1...
        for ip, count in packet_count.items():  #Our for loop will execute either rating through the packet counts for each IP.
            packet_rate = count / time_interval #We can then calculate the packet rate by dividing the count by the time interval.
                                                #(EX: if there were 40 packets and one second pass, packet weight would be 40 packets a second.)
            #print(f"IP: {ip}, packet rate: {packet_rate}") -> Shows the current IPs and rates it detects.
            if packet_rate > THRESHOLD and ip not in blocked_ips:      #We can see if the packet rate exceeds the threshold set earlier, it also checks if a IP has been blocked.
                print(f"Blocking IP: {ip}, packet rate {packet_rate}") #Printing a message to let us know if the IP is being blocked.
                os.system(f"iptables -A INPUT -s {ip} -j DROP") #This blocks the IP address using the iptables command with the OD system function.
                blocked_ips.add(ip) #Adding the blocked IP to a Blocked IP set to keep track of.
        
        #Clearing the packet count dictionary and restart the time so that we can repeat the process.
        packet_count.clear()
        start_time[0] = current_time

#Declaring the main function, used mainly for checking root priveliges, initializing packet count and start time variable as well as starting the packet snapping
#process with a specified callback function.
if __name__ == "__main__":  #Main guard and main function has been combined. An alternative way of write it.
    if os.geteuid() !=0:    #We check to make sure the script has been executed using root priveliges. 1. To access raw network traffic, and 2. to block an IP we need to confic firewall.
        print(f"This script require root privileges.")  #In case we don't have access to the root
        sys.exit(1) #Exits the script with an error code.
        
    packet_count = defaultdict(int) #We initialize the packet count dict with a default dict. We use the default dict due to its ability to assign a default value ie0 to a new IP when first encountered.
    start_time = [time.time()] #We record the start time of the script in the list.
    blocked_ips = set() #And initialize a blocked IPS set to store blocked IPs.
    
    print(f"Monitoring Network traffic...") #Lets the user know know the process has started.
    sniff(filter="ip", prn=packet_callback) #Starts sniffing IP packets and pass them to the packet callback function for analysis.
    
#Note: euid = effective user id.
#Linux Script.
