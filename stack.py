def valid_parenthesis(s):
    stack = []

    missing = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }

    for ch in s:
        if stack and ch in missing.values():
            stack.append(ch)
        else:
            if not stack and stack[-1] != missing[ch]:
                return False
            stack.pop()
    return len(stack) == 0