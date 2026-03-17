# RECURSION PRACTICE

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
# print(factorial(5))
def sum_n(n):
    if n < 0:
        return "invalid input"
    if n <= 1:
        return n
    return n + sum_n(n - 1)
# print(sum_n(5))

# ARRAT PRACTICE
def two_sum_sorted(arr, target):
    n = len(arr)
    i = 0
    j = n-1
    while i< j:
        current_sum = arr[i] + arr[j]
        if current_sum == target:
            return [i, j]
        if current_sum < target:
            i += 1
        else:
            j -= 1
    return -1
# print(two_sum_sorted(arr = [2, 7, 11, 15],target = 9))

def two_sum_unsorted(arr, target):
    n = len(arr)
    seen = {}
    for i in range(n):
        need = target - arr[i]
        if need in seen:
            return [seen[need],i]
        else:
            seen[arr[i]] = i
    return -1
# print(two_sum_unsorted(arr = [11, 15, 2, 7],target = 9))