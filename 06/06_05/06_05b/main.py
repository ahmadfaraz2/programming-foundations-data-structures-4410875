from collections import deque


def check_matching_parenthese(string):
    stack = deque()

    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


print(check_matching_parenthese("(Hello world)"))

print(check_matching_parenthese("Hey there)"))
