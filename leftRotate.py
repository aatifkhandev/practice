# arr[] = {1,2,3,4,5}
# op:
#  2,3,4,5,1

def leftRotate(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
        
    arr[n-1] = temp



def rightRotate(arr,n):
    temp = arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1] = arr[i]
        
    arr[0] = temp    
    
    
arr = [1,2,3,4,5]
n = len(arr)
rightRotate(arr,n)

for i in range(n):
    print(arr[i])