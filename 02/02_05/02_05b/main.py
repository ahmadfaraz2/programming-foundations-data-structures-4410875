seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"],
]

# access Lauren
print(seating_chart[2][1])

"""
enumerate( iteratable ) function allow us to loop through the list
while giving us access to a counter and the value of each item in the iterable.
"""

for i, row in enumerate(seating_chart):
    print(f"Row {i+1} contain {row}")


for i, row in enumerate(seating_chart):
    for j, student in enumerate(row):
        print(f"{student} sits in row {i+1} at seat {j+1}")
