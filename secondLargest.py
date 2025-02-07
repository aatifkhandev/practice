def secondLargest(arr,n):
    if n<2:
        return -1
    max = arr[0]
    sL = -1
    for i in range(n):
        if arr[i] > max:
            sL = max
            max = arr[i]
            
        elif arr[i]>sL and arr[i]!=max:
            sL = arr[i]
            
            
    return sL

def secondSmall(arr,n):
    if n<2:
        return -1
    min = arr[0]
    secondS = float('inf')  # Initialize to a very large value
    for i in range(n):
        if arr[i] < min:
            secondS = min
            min = arr[i]
        elif arr[i]<secondS and arr[i]!=min:
            secondS=arr[i]
    return secondS




arr = [1,2,3,4,5]
n = len(arr)
print(secondSmall(arr,n))