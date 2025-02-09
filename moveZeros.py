


def moveZeros(n: int,  arr: [int]) -> [int]:
    j = -1
    # Place the pointer j
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    
    # No non-zero elements
    if j == -1:
        return arr
    
    # Move the pointers i and j and swap accordingly
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    return arr


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = moveZeros(n, arr)
for it in ans:
    print(it, end=' ')
print()