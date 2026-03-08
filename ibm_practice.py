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
# print(longest_consecutive_brute(arr))

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

# print(longest_consecutive_optimize(arr))

def two_sum(arr, k):
    n = len(arr)
    res = [-1, -1]
    for i in range(n):
        for j in range(i+1, n):
            sum = arr[i] + arr[j]
            if sum == k:
                res[0] = i
                res[1] = j
            sum = 0
    return res
# arr = [100, 4, 200 ,1,2,3]
# print(two_sum(arr, 2000))

def two_sum_using_hashing(arr, k):
    n = len(arr)
    res = [-1, -1]
    hash_arr = {}
    for i in range(n):
        need = k - arr[i]
        if need in hash_arr:
            res[0] = need
            res[1] = arr[i]
            return res
        hash_arr[arr[i]] = i
    return res
# arr = [100, 4, 200 ,1,2,3]
# print(two_sum_using_hashing(arr, 2000))

def longest(arr, k):
    n = len(arr)
    max_len = 0
    mp = {}
    prefix_sum = 0
    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum == k:
            max_len = i + 1
        
        if (prefix_sum - k) in mp:
            max_len = max(max_len, i - mp[prefix_sum - k])

        if prefix_sum not in mp:
            mp[prefix_sum] = i
    return max_len

arr = [100, 4, 200 ,1,2,3]
print(longest(arr, 207))

