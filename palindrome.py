# Input:N = 4554
# Output:Palindrome Number


def palindrome(n):
    revNum = 0
    og = n
    while(n>0):
        ld = n%10
        revNum = (revNum*10)+ld
        n = n//10
    if og == revNum:
        print("Palindrome")
    else:
        print("Not a palindrome")
    

n = 4553
palindrome(n)