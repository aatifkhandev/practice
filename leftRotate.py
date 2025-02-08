# arr[] = {1,2,3,4,5}
# op:
#  2,3,4,5,1

def leftRotate(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
        
    arr[n-1] = temp
    
    
    
arr = [1,2,3,4,5]
n = len(arr)
leftRotate(arr,n)

for i in range(n):
    print(arr[i])