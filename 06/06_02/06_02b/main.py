# Using List as Stack

card_stack = []

card_stack.append("Jack of Hearts")  # bottom
card_stack.append("2 of Diamonds")
card_stack.append("10 of Spades")  # top

# front(bottom) ---- back(top)
top_card = card_stack.pop()
print(top_card)
top_card = card_stack[-1]
print(top_card)


if not card_stack:
    print("Card Stack is empty!")
else:
    print(len(card_stack))


print(card_stack)
