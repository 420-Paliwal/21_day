# binary search 

def binary_search(arr, x):
    low = 0 
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
        
    return -1

# binary search first occurance

def binary_search_first_occ(arr, target):
    low = 0 
    high = len(arr)-1
    ans = -1
    while low <= high:
        mid = (low + high)//2

        if arr[mid] == target:
            ans = mid
            high = mid -1
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        
    return ans

# binary search first occurance

def binary_search_last_occ(arr, target):
    low = 0 
    high = len(arr)-1
    ans = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            ans = mid
            low = mid + 1
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return ans