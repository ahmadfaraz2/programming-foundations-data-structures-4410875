# Linear Search

"""
It is also called Squential Search, it is easy but it is so slow if there is 
large amount of data.
"""


my_list = [5, 3, 1, 6, 2, 7, 8]

item = 6


def search(item, listy):
    for element in listy:
        if element == item:
            return True
    return False


print(search(item, listy=my_list))


item_index = my_list.index(item)  # Also a Linear Search
print(item_index)
