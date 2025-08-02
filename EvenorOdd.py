num = int(input('Enter a number:')) #Prompts the user to enter a number. Input() always returns a string, so int() converts it into an integer and stores it in the variable num
if (num % 2) == 0: #% is the modulus operator, which gives the remainder after division. If a number divided by 2 has a remainder of 0, it's even. Checks this line: "is the number divided by 2?"
    print('{0} is Even'.format(num)) #if the condition is true, this prints "[number] is even". format(num) puts the number into {0}.
else:
    print('{0} is Odd'.format(num))
#If the number isn't devisible by 2, it must be odd, so this prints "[number] is odd".
