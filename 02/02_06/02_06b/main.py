# Tuples are immutable array-like structures

point = (2, 5)

print(point[0])
print(point[1])


def calculate_square_prop(side_length):
    area = side_length * side_length
    perimeter = 4 * side_length
    return (area, perimeter)


result = calculate_square_prop(3)
print("Area: ", result[0])
print("Perimeter: ", result[1])
