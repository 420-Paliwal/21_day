def max_value(arr):
    n = len(arr)
    if n == 0:
        return None
    if n == 1:
        return arr[0]
    largest = arr[0]
    for i in range(1,n):
        if arr[i] > largest:
            largest = arr[i]
    return largest


def isSorted(arr):
    n = len(arr)
    if n == 0:
        return None
    if n == 1:
        return arr[0]
    
    
def twosum(arr,x):
    mp = {}
    for i, num in enumerate(arr):
        need = x-num
        if need in mp:
            return [mp[need],i]
        mp[num]=i
    return None


def maxSumSubarray(arr, k):
    window_sum = sum(arr[0:k])
    max_sum = window_sum
    for i in range(k,len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i-k]

        max_sum = max(max_sum, window_sum)
    
    return max_sum


def longest_subarray(arr, k):
    left = 0
    curr_sum = 0
    max_len = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1
        max_len = max(max_len, i-left+1)
    return [max_len, curr_sum]

arr = [10, 14,3,54,33,23,45,43,83,84,22,545,3526,853,5742]
print(longest_subarray(arr,10000))