from collections import deque

history_stack = deque()


history_stack.append("https://google.com")  # bottom
history_stack.append("https://linkedin.com")
history_stack.append("https://stackoverflow.com")  # top


print(history_stack[-1])
print(history_stack.pop())
