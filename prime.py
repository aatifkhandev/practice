
# Input:N = 2
# Output:True
# Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).



# Input:N =10
# Output: False
# Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10.


import math

# Function to check if a
# given number is prime.
def checkPrime(n):
    # Initialize a counter variable to
    # count the number of factors.
    cnt = 0

    # Loop through numbers from 1
    # to the square root of n.
    for i in range(1, int(math.sqrt(n)) + 1):
        # If n is divisible by i
        # without any remainder.
        if n % i == 0:
            # Increment the counter.
            cnt = cnt + 1

            # If n is not a perfect square,
            # count its reciprocal factor.
            if n // i != i:
                cnt = cnt + 1

    # If the number of
    # factors is exactly 2.
    if cnt == 2:
         # Return true, indicating
         # that the number is prime.
        return True
    # If the number of
    # factors is not 2.
    else: 
        # Return false, indicating
        # that the number is not prime.
        return False
    
n = 4
if(checkPrime(n)):
    print("prime")
else:
    print("not a prime")