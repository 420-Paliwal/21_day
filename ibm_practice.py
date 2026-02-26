def longest_consecutive_brute(arr):
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
print(longest_consecutive_brute(arr))

def longest_consecutive_optimize(arr):
    n = len(arr)
    max_len = 0
    new_set = set(arr)
    for num in new_set:
        if num - 1 not in new_set:
            current = num
            count = 1
            while current + 1 in new_set:
                current += 1
                count += 1
            
            max_len = max(max_len, count)
    return max_len

arr = [100, 4, 200 ,1,2,3]
print(longest_consecutive_optimize(arr))