primary_colors = set(["red", "green", "blue"])

print(primary_colors)

color = "yellow"

if color in primary_colors:
    print(color + " is a primary color")
else:
    print(color + " is not a primary color")

letters = set(["a", "b"])
letters.add("c")

print(letters)
