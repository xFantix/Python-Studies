def CheckBrackets(brackets):
    stack = []
    pairs = {')': '(', ']': '['}

    for char in brackets:
        if char in ['(', '[']:
            stack.append(char)
        elif char in [')', ']']:
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return not stack

input = input()
result = "Correct" if CheckBrackets(input) else "Incorrect"

print(result)