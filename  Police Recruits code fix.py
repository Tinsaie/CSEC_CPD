n = int(input())
events = list(map(int, input().split()))

available_officers = 0
untreated_crimes = 0

for event in events:
    if event == -1:
        if available_officers > 0:
            available_officers -= 1
        else:
            untreated_crimes += 1
    else:
        available_officers += event

print(untreated_crimes)
