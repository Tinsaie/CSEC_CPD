s = input()
total_rotations = 0
current_position = ord('a')

for char in s:
    target_position = ord(char)
    clockwise_rotations = abs(target_position - current_position)
    counterclockwise_rotations = 26 - clockwise_rotations
    total_rotations += min(clockwise_rotations, counterclockwise_rotations)
    current_position = target_position

print(total_rotations)
