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