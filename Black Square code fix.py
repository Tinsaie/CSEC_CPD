a1, a2, a3, a4 = map(int, input().split())
s = input()
total_calories = 0

for char in s:
    if char == '1':
        total_calories += a1
    elif char == '2':
        total_calories += a2
    elif char == '3':
        total_calories += a3
    elif char == '4':
        total_calories += a4

print(total_calories)
