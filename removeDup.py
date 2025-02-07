def removeDup(arr,n):
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    
    k = len(st)
    j = 0
    for x in st:
        arr[j] = x
        j+=1
    return k
        
        
def removeDupOptimized(nums,n):
    i = 0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
                i+=1
                nums[i] = nums[j]

    return i+1

arr = [1,1,1,2,2,2,3,3,3]
n = len(arr)
ans = removeDupOptimized(arr,n)
for i in range(ans):
    print(arr[i])