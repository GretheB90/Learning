import nmap #nmap is a Python wrapper for the nmap network scanner.

nm = nmap.PortScanner() #Creates an instance of the nmap.portscanner class, then assing to the variable/name: nm

#Set the target IP range:
target = "8.8.8.8" #Address to Nmap site, need to change due to needing permission to scan domain. A /25 means “scan 128 houses” (from .0 to .127).
#Set scan options:
options = "-sV -sC -v" #sV = gives us version info about the services found on those ports. cS = Nothing fancy, want to run a standard and matte script.

#options speficies how the scan should run:
# -sV: Service version detection (try to find out what services are running on each port). Tell me what’s running inside each open door
# -sC: Run default nmap scripts (useful for vulnerability detection, banner grabbing, etc). Use some built-in spy scripts to look for common problems or info
# -v: "verbose" mode. Means more talkative or giving more details
# Analogy: nmap is a mailman checking houses on your street.
# Without -v, the mailman just tells you "Done" when finished.
# With -v, the mailman tells you which houses he’s visiting and what he sees as he goes.

#Run the scan with exception handling:
try:
    print("Starting scan...")
    nm.scan(target, arguments=options) #Runs the scan on the IP range using the specified Nmap options.
    print("Scan complete!")
except Exception as e:
    print(f"Error while scanning: {e}")
    exit() #Stop program on error.
#the scanner goes house to house, checking ports and gathering info

filename = "scan_results.txt"

#Open a file to scan results:
with open(filename, "w") as f:
    #Loop over each host found in the scan:
    for host in nm.all_hosts():
        f.write(f"Host: {host} ({nm[host].hostname()})\n") #Nested loop structure(2 loops). Will print info about each host protocol and port that was discovered. You’re going through every house (computer) the scanner found
        f.write(f"State: {nm[host].state()}\n") #Outer loop. Iterates through the list of hosts returned by the underscore host methods of the nmap.portscanner instance
    
    #Loop over each protocol (tcp/udp):
        for protocol in nm[host].all_protocols(): #Inner loop. For protocol in nm hosts. It will go through the list of protocols used by the individual hosts. Returns a list of protocols.(TCP, UDP)
            f.write(f"Protocol: {protocol.upper()}\n") #TCP (like a telephone with a stable connection), Or UDP (like sending paper airplanes — faster but riskier)
            port_info = nm[host][protocol]
        
    #Loop over each port and get details:
        for port in sorted(port_info.keys()): #Innermost loop. Iterates through the list of ports and their states for the current protocol. Using the Items method.
            info = port_info[port]
            state = info.get("state", "unknown")
            name = info.get("name", "unknown")
            product = info.get("product", "")
            version = info.get("version", "")
            extrainfo = info.get("extrainfo", "")
            cpe = info.get("cpe", "")
            
            f.write(f"Port: {port}\n")
            f.write(f"  State: {state}\n")
            f.write(f"  Service: {name}\n")
            if product.strip():
                f.write(f"  Product: {product} {version}\n")
            if extrainfo:
                f.write(f"  Extra Info: {extrainfo}\n")
            if cpe:
                f.write(f"  CPE: {cpe}\n")
        f.write("\n")

print(f"Scan results saved to {filename}")

#Print results to console/Terminal too:
for host in nm.all_hosts():
    print(f"\nHost: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")

    for protocol in nm[host].all_protocols():
        print(f"Protocol: {protocol.upper()}")
        port_info = nm[host][protocol]

        for port in sorted(port_info.keys()):
            info = port_info[port]
            state = info.get("state", "unknown")
            name = info.get("name", "unknown")
            product = info.get("product", "")
            version = info.get("version", "")
            extrainfo = info.get("extrainfo", "")
            cpe = info.get("cpe", "")

            print(f"Port: {port}")
            print(f"  State: {state}")
            print(f"  Service: {name}")
            if product.strip():
                print(f"  Product: {product} {version}".strip())
            if extrainfo:
                print(f"  Extra Info: {extrainfo}")
            if cpe:
                print(f"  CPE: {cpe}")
