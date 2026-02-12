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