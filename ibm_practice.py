def consecutive(arr):
    n = len(arr)
    arr.sort()
    max_len = 1
    count = 1
    i = 0
    for i in range(1,n):
        if arr[i] == arr[i-1]+1:
            count += 1
        else:
            max_len = max(max_len, count)
            count = 1
    return max(max_len, count)

arr = [100, 4, 200 ,1,2,3]
print(consecutive(arr))