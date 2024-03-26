set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}


union_set = set_A.union(set_B)  # combine the sets (uniques values)
print(union_set)


intersection_set = set_A.intersection(set_B)  # common enteries in both sets
print(intersection_set)


difference_set = set_A.difference(set_B)  # subtracting set_B from set_A (setB - SetA)
print(difference_set)


difference_set_BA = set_B.difference(set_A)  # return all the items unique to B
print(difference_set_BA)

# print all elements that are unique to A and B.
symmetric_difference = set_A.symmetric_difference(set_B)
print(symmetric_difference)
