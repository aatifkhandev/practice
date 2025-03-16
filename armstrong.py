#  Given an integer N, return true it is an Armstrong number otherwise return false.

# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

# Input:N = 153
# Output:True
# Explanation: 13+53+33 = 1 + 125 + 27 = 153

# Input:N = 371
# Output: True
# Explanation: 33+53+13 = 27 + 343 + 1 = 371

def armstrong(n):
    og = n
    sum = 0
    while n>0:
        lastDigit = n%10
        sum+=(lastDigit*lastDigit*lastDigit)
        n = n//10
    if sum == og:
        print("yes")
    else:
        print("no")
        
        
        
n = 153
armstrong(n)