import re

#First we make a dict and put the values into the variable, "Count".
#to make sure it works, we use a print() to make sure it gets the added text in "line".
Count = dict() #Creates an empty dictionary to store the count of each word
print('Enter some text here:') #It prints the prompt, but doesn't take the users input as it's hardcoded in "line".
line = 'The wolf showed up outside the house where the pigs resided! He blew and he blew and the house fell down into pieces. The pigs where scared to heck!' #input('') The text to be analyzed.
#line = re.sub(r'[^\w\s]', '', line)
#line = line.lower()
#line = re.sub(r'[^\w\s]', '', line.lower())
line = re.sub(r'[^\w\s]', '', line).lower() #removes ! and punctuations and makes the text lowercase.

#We're now splitting a string into a list of substrings, based on space, tabs or newlines as seperators and adds it into the words variable.
words = line.split(' ') #Note: punctuation (like !, .) will stick to the words. e.g., "see!" is different from "see".

#We again print out the current result to check it all works still after the latest code implementation.
print('Words:', words) #Prints the list of words you got from splitting the sentences.

#This loop goes through each word in the list:
#count.get(word, 0) tries to get the current count of the word from the dictionary.
#if the word isn't there yet, it returns 0.
#+1 increases the count.
#it saves the new count back into the dictionary under that word.
print('Counting...')
for word in words:
    Count[word] = Count.get(word,0)+1
print(Count) #It prints the dictionary showing how many times each word appeared.

#I've learned I need to also be aware that words like "The" and "the" are treated as different because they're case-sensitive.
#To make it case-sensitive, I could add (word.lower() )
