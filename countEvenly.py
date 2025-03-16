# Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder). Return the total number of such digits.

# A digit d of n divides n evenly if the remainder when n is divided by d is 0 (n % d == 0).
# Digits of n should be checked individually. If a digit is 0, it should be ignored because division by 0 is undefined.


# Input: n = 12
# Output: 2
# Explanation: 1 , 2 when both divide 12 leaves remainder 0.



def evenlyDivides(n):
    count = 0
    og = n
    while n > 0:
        d = n % 10 
        if og % d == 0 and d!=0:
            count+=1
        n//=10
    return count
        

    
    
n = 12468
print(evenlyDivides(n))

