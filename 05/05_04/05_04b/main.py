from collections import deque


def print_binary_nums(num):
    if num <= 0:
        return

    queue = deque()
    queue.append(1)

    for i in range(num):
        binary = queue.popleft()
        print(binary)
        queue.append(binary * 10)
        queue.append(binary * 10 + 1)


print_binary_nums(5)
print()
print_binary_nums(-9)
print()
print_binary_nums(10)
