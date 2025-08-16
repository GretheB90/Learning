import psutil #Lets us look at all the apps and programs running in the computer.
import datetime #Lets us write down the time and date when we do the scan.

#File where suspicious process logs will be saved.
LOG_FILE = "keylogger_scan_report.txt"

def detect_keylogger(): #Main function. Our "detective".
    #List of suspicious process names that could belong to keyloggers.
    suspicious_processes = ["keylogger", "logkeys", "xinput"] #Names of keylogger processes
    
    found_suspicious = False  # Flag to track if anything was found
    
    #Get current timestamp for the log
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entries = [f"\n--- Scan at {timestamp} ---\n"]
    
    #Iterate through running processes
    for proc in psutil.process_iter(["pid", "name"]): #Each proc is like one entity. Ex: Classroom and check each students names.
        try:
            #Check if process name matches any of the suspicious names
            process_name = proc.info["name"]
            if process_name:
                process_name_lower = process_name.lower()
                if any(susp_name in process_name_lower for susp_name in suspicious_processes):
                    found_suspicious = True
                warning_msg = f"[!] Suspicious process detected: {process_name} (PID: {proc.info['pid']})" #PID = Process ID.
                print(warning_msg)
                log_entries.append(warning_msg)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        #If they already left, no permission granted to check or acting weird, like zombies. We skip these.
        
    # If anything suspicious was found, log it
    if found_suspicious:
        with open(LOG_FILE, "a") as log_file:
            log_file.write("\n".join(log_entries))
            log_file.write("\n")
    else:
        print("[*] No suspicious processes found.")
        
#Run the detector

if __name__ == "__main__":
    print("[+] Running keylogger detection...")
    detect_keylogger()
    print("[+] Scan complete.")
