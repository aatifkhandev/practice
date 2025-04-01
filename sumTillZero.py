# Finding the Sum of Digits of a Number Until Zero
# Description: Write a program to repeatedly sum the digits of a number until the result is zero.
# Example:
# Input: number = 123
# Output: 6
# Explanation: Sum of digits is 1 + 2 + 3 = 6; sum of digits of 6 is 6 (which is a single digit).

def sumOfDigits(n):
    sum = 0
    while n>0:

        ld = n%10
        n = n//10
        sum +=ld
        
    while sum>10:
       return sumOfDigits(sum)
        
    return sum
        




print(sumOfDigits(12345))
