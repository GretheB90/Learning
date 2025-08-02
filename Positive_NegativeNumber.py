#Check if a number is Positive or Negative:

#num = float(input('Enter a number: '))
#if num >0: #Greater than
    #print('Positive Number, Alright!')
#elif num == 0: #Equals to
    #print('Zero!')
#else:
    #print('Negative Number, Yo!')

    
#Nested if version:

num = float(input('Enter a number: '))
if num >= 0: #Greater than or Equal than
    if num == 0: #Equals to
        print('Zero!')
    else:
        print('Positive Number')
else:
    print('Negative Number, Yo!')

#Float allows for numbers with Decimals rather than only full number.
#If a number is greater than 0, it's positive.
#This is being checked in the if expression.
#If the number is False, the number will either be zero or a negative value.
