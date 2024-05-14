def valid_parentheses(s: str)->bool:
    stack = []
    parentheses = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            if not stack or parentheses[char] != stack.pop():
                return False
    return not stack;