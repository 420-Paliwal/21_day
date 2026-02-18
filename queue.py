# Sliding window maximum brute force 
def sliding_window_max(arr, k):
    n = len(arr)
    res = []
    for i in range(n-k+1):
        maxx = arr[i]
        for j in range(i+1, k+i):
            if arr[j] > maxx:
                maxx = arr[j]

        res.append(maxx)
    return res

# Sliding window maximum (OPTIMIZED APPROACH.....)
from collections import deque

def sliding_window_maxx_optimized(arr, k):
    n = len(arr)
    dq = deque()
    res = []

    for i in range(n):
        if dq and dq[0] <= i-k:
            dq.popleft()
        
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k-1:
            res.append(arr[dq[0]])
        
    return res

# Sliding window minimum (OPTIMIZED APPROACH.....)
from collections import deque

def sliding_window_min_optimized(arr, k):
    n = len(arr)
    dq = deque()
    res = []

    for i in range(n):
        if dq and dq[0] <= i-k:
            dq.popleft()
        
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k-1:
            res.append(arr[dq[0]])
        
    return res

# First negative index 

def first_negative(arr, k):
    n = len(arr)
    dq = deque()
    result = []

    for i in range(n):
        if arr[i] < 0:
            arr.append(i)

        if dq and dq[0] <= i-k:
            dq.popleft()
        
        if i>=k-1:
            if dq:
                result.append(arr[dq[0]])
            else:
                result.append(0)

    return result