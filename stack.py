def valid_parenthesis(s):
    stack = []
    missing = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }
    for ch in s:
        if ch in missing.values():
            stack.append(ch)
        else:
            if not stack and stack[-1] != missing[ch]:
                return False
            stack.pop()
    return len(stack) == 0

print(valid_parenthesis("(){}[]"))

def next_greater(arr):
    n = len(arr)
    stack = []
    result = [-1]*n
    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result

print(next_greater([4,5,2,10,8]))

def stock_span(prices):
    n = len(prices)
    stack = [] 
    span = [0] * n
    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        if not stack:
            span[i] = i + 1
        else:
            span[i] = i-stack[-1]
        stack.append(i)
    return span
print(stock_span([100, 80, 60, 70, 60, 75, 85]))

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self):
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]
    
    def minn(self):
        return self.minstack[-1]

def next_smaller(arr):
    n = len(arr)
    stack = []
    result = [-1]*n

    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])
    
    return result

print(next_smaller([4,8,5,2,25]))

def daily_temp(arr):
    n = len(arr)
    stack = []
    result = [0]*n

    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] - i
        stack.append(i)
    
    return result