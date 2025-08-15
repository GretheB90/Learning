nums = range(2,1000) #List of numbers from 2 and all the way to 999.

def is_prime(num):
    for x in range(2,num):
        if (num%x) == 0:
            return False
    return True

primes = list(filter(is_prime, nums))

print(primes)

#If any of those numbers divides evenly (no remainder), it's not a prime
#If nothing divides it evenly, it's a prime!
#Prime number: Only divisible with 1 and itself.
