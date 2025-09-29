import win32api     #“Hey Python, get the special Windows tool that lets me talk to the mouse and other things.”
import time         #"Hey Python, I want to use the clock and timer tools from the time module."
import os           #Helps your program talk to your computer, like asking "Where am I?" or "What files are here?"

try:
    while True: #Keeps running forever (until you stop it).
        #Get the mouse position
        x, y = win32api.GetCursorPos() #Gets your current mouse position.
        
        #Clear the screen(For cleaner output)
        #Clears the terminal so only one position shows at a time (Windows).
        os.system('cis') #Use 'clear' instead if on Linux/Mac
        
        #print current position
        print(f"Mouse position_ X={x}, Y={y}")
        
        #Wait a short moment so it doesn't go too fast
        time.sleep(0.1) #Waits 0.1 seconds before checking again

except KeyboardInterrupt: #If you press Ctrl + C, it stops nicely
    print("\nStopped tracking.")
