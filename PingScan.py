import ipaddress    #imports the IP address Module/For IP network calculations
import math         #imports the Math Module
import os           #Provides functions for interacting with the Operating system/For file path handling
import pandas as pd #Panda, usually imported under the pd alias

def subnet_calculator(network, num_subnets): #function to call in the subnet_calculator.
    #Takes in a network and the amounts of subnets we're looking for.
    try: #This starts the script
        network = ipaddress.IPv4Network(network, strict=False)  #The False makes it so that if our net and IP doesn't align, we can still use them together.
                                                                #Parses the string input (e.g., "192.168.10.24") into an IP object.
                                                                #Strict=False allows addresses like "192.168.10.5/24" (Not just perfect base network addresses).
        new_prefix_len = network.prefixlen + math.ceil(math.log2(num_subnets))  #Calculates the new prefix lenght based on how many subnets you need.
                                                                                #log2(num_subnets) gives the number of extra bits needed for that many subnets.
                                                                                #math.cell ensures we round up to cover all subnets.
        subnets = list(network.subnets(new_prefix=new_prefix_len)) #Generates subnets using the new prefix.
        if len(subnets) < num_subnets: #if len(subnets) is less than num_subnets. Checks if we have enough subnets to satisfy the user's request.
            raise ValueError('Not enough subnets available')
        
        results = [] #Array for results from the list below
        for subnet in subnets[:num_subnets]:
            result = {
                'Subnet Network Address': str(subnet.network_address),
                'Broadcast Address': str(subnet.broadcast_address),
                'Subnet Mask': str(subnet.netmask),
                'Number of usable Hosts': subnet.num_addresses - 2,
                'First Usable Host': str(subnet.network_address + 1),
                'Last Usable Host': str(subnet.broadcast_address - 1)
            }
            #Standard Subnet details: Usable hosts = total IPs minus 2 (network and broadcast addresses are not usable).
            #+1 and -1 are used to get the first and the last usable IPs.
            results.append(result) #Append: Add "items" to the result array.
        return results
    except ValueError as e: #If anything fails, it will send us to an error/stop instead (e.g., too many subnets requested).
        return [{'Error': str(e)}]
    
def main():
    network = input('Enter the network address (e.g. 192.168.10./24): ')
    num_subnets = int(input('Enter the number of subnets: '))
    
    results = subnet_calculator(network, num_subnets)
    
    df = pd.DataFrame(results)
    #Runs the calculator and loads results into a Pandas DataFrame (like a spreadsheet).
    
    scripts_dir = os.path.dirname(os.path.realpath(__file__))
    
    output_file = os.path.join(scripts_dir, 'subnet_calculator_output.csv')
    df.to_csv(output_file, index=False) #df = Dataframe.
    #Figures out the current script's directory.
    #Saves the result as subnet_calculator_output.cvs in that directory.
    print(f'Results saved to {output_file}') #Saves and shows the results in a readable file format of choice decided in line 41 (df.to_cvs)
    
if __name__ == '__main__':
    main()
#This ensures the main() function runs only if the script is run directly - not if it's imported as a module.

#If you input:
#Enter the network address: eg. 192.168.1.1
#Enter the number of subnets: eg. 4
#You will get 4 subnet blocks written to CVS with all the details: usable IPs, broadcast address, etc.
    
#Len = Returns the number of elements(lengt) in an iterator/object passed to the function.
#math.ceil (line.10) rounds a number UP to the nearest integer, if necessary.
