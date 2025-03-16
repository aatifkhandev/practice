# Input:N = 36
# Output:[1, 2, 3, 4, 6, 9, 12, 18, 36]
# Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.
import math

def printDivisors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i)

# def printDivisorsOptimized(n):
#     for i in range(1,int(math.sqrt(n+1))):
#         if n % i == 0:
#             print(i)
#         if ((n/i)!=i):
#             print((n/i))

import math

def printDivisorsOptimized(n):
    divisors = []  # To store smaller divisors
    for i in range(1, int(math.sqrt(n)) + 1):  # Iterate till sqrt(n)
        if n % i == 0:
            divisors.append(i)  # Store the divisor
            if i != n // i:  # Avoid printing the square root twice if it's a perfect square
                print(n // i)  # Print the complementary divisor
    for divisor in divisors:
        print(divisor)  # Print the smaller divisors in increasing order

# Test the function
n = 36
printDivisorsOptimized(n)
