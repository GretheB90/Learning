import win32api     #“Hey Python, get the special Windows tool that lets me talk to the mouse and other things.”
                    #win32api only works on Windows computers. It's like a secret power only Windows knows.

print("Press Enter to get mouse position...")   #Press Enter when you're ready
input()                                         #Waits until you press the Enter key

location = win32api.GetCursorPos()      #The computer looks at your screen and gets the exact spot your mouse is sitting.
print("This is where you are:", location)   #Gives back something like: (500,300). 500 pixels from the left|300pixels from the top.

input("Press Enter to close...")    #The program waits one more time before closing, so you have a chance to see the answer.
