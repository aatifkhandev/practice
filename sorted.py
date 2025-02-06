def sorted(arr,n):
    
    for i in range(n):
        if arr[i-1] < arr[i]:
            return True
    return False


arr = [1,2,3,4,7,8]
n = len(arr)
print(sorted(arr,n))
    