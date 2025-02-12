s = input()
t = input()

position = 0  # Liss starts at position 0 (the first stone)

for instruction in t:
    if position < len(s) and s[position] == instruction:
        position += 1  # Move forward if the instruction matches the current stone color

print(position + 1)  # Output the final position (1-based index)
