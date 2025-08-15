import math

def is_prime(num):
    for x in range(2, int(math.sqrt(num)) +1): #sqrt = Square root. (Example: math.sqrt(25) = 5. Because 5x5=25)
        #Loop through all numbers from 2 up to the square root of num, and check if any of them divide num
        if num % x == 0:
            return False
        return True
    
primes = [num for num in range(2, 1000) if is_prime(num)]
print(primes)

#Handles bigger numbers faster.
