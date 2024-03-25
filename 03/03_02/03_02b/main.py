# Key: State
# Value: Capital

states_to_capital = {
    "New York": "Albony",
    "Texas": "Austin",
}


print(states_to_capital["Texas"])
print("~~~~~~~~~~~~~~~~~~~~")

# Retrive keys
for key in states_to_capital.keys():
    print(key)
print("~~~~~~~~~~~~~~~~~~~~")


# Retrive keys and values
for key, value in states_to_capital.items():
    print(key + " | " + value)
