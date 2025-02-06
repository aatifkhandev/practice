def largest(arr,n):
    max = arr[0]
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [1,2,3,4,5,6,7]
n = len(arr)
print(largest(arr,n))