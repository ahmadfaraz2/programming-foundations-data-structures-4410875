def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)
    return sorted_list[1]
    # for element in sorted_list:
    #     if element == sorted_list[1]:
    #         return element
    # return "You're again wrong!"


def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None

    smallest_num = float("inf")
    second_smallest_num = float("inf")
    for num in my_list:
        if num < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = num
        elif num < second_smallest_num:
            second_smallest_num = num
    return second_smallest_num


print(find_second_smallest_v2([5, 8, 3, 2, 6]))
