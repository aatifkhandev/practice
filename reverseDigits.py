# Input:N = 12345
# Output:54321

def reverse1(n):
    revNum = 0
    while(n>0):
        ld = n%10
        revNum = (revNum*10)+ld
        n//=10
    return revNum
    

n = 12345
print(reverse1(n))