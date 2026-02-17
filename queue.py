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

arr = [1,3,-1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(arr, k)) 