# Frozen sets are immutable

primary_color = frozenset(["blue", "green", "red"])

if "blue" in primary_color:
    print("Blue is in set!")

# primary_color.add("yellow")
