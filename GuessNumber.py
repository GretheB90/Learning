# Guess Number Game:
import random #Gives us the tools to generate random numbers and make random choices.

Answer = random.randint(1, 99) #Makes it possible to be a random integer between 1 to 99 and stores it to the variable Answer.
IsRunning = True #This can be removed if desired - see line 10. A flag to control the game loop. As long as it's True, the program keeps running.

#print(Answer)

print('guess a number between 1 and 99') #Displays instructions to the player
while IsRunning == True: #while True - Starts a loop that keeps asking until the player gets it right.
    Guess = input('what\'s your guess: ') #Asks a player to type in a guess.
    #print('the users guess was...')
    #print(Guess)
    IsNum = Guess.isdigit() #Checks if the guess is made up of digits only (e.g., "69" is valid, while "hello" or "30.5" is not).
    #print('is guess a digit?')
    #print(IsNum)
    if IsNum == False: #If input isn't a number, the game goes back to the top of the loop.
        print('You lose, dumbo')
        continue
    Guess = int(Guess) #Converts the string input into an integer.
    if Guess < 1 or Guess > 99:
        print('Lmao no number between 1 and 99?') #If the number is outside the valid range (1-99), it give an error and loops again.
        continue
    
    #From line 10 and 21 it shows the program running, were we can input a guess. 
    #Guess.isdigit at this point allows for both numbers and letters to be accepted, though only numbers show true.
    #If we guess a string aka letters, we get the message; you lose, dumbo.
    #The continue brings us then back to the start of the program to re-do our guess.
    #We now know that the Guess variable only contains numbers, thus we can convert our Guess variable into actual numbers.
    #We can use int(Guess) and make it specifically accept anything between 1 and 99 by using comparison inside an if-statement. 
    #Letters and numbers lower or higher than the set values will show False/incorrect.
    #The program brings us back to the beginning if we guess wrong and the cycle continues.
    #About Parsing one format to another, look int(Guess).
    
    #Did the user guess correctly?
    if Guess == Answer: 
        print('You got it right, Amazing!') #If the guess matches the answer, it stops the loop (isRunning = False), and continues to the end(print())
        IsRunning = False
        continue
        #break
    elif Guess > Answer:
        print('Too high! Go lower!')
        continue
    else:
        print('Too low, too slow')
        continue
print('End of Program') #This message prints after the user gets the right asnwer and the loop ends.


#What have I learned through this project:
#About the basic use of if (a statement and a keyword), elif or else (keywords, but can also be a statement if having a : following) and basic Conditionals. 
#About continue is to make a program go back to its "starting point"(in this context by skipping the current iteration, and break to exit a loop entierly).
#About assignments and how it assigns values to variables and how a variable acts as a "container" to store data.
#About integers as how it is a whole number. (no decimals which would make it a float).
#About strings being a representation of text data.
#About conversion which is helpful to convert values from one type to another. (In this context, we changed it from being a digit into a integer)
#About functions which are the sections of a code that performs a specific task. It also can contain an argument. 
#About arguments and how they are a value we pass into a function for it to be called later in the script. 
