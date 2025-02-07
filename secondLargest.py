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





arr = [1,2,3,4,5]
n = len(arr)
print(secondLargest(arr,n))