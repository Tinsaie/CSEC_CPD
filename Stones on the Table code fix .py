n = int(input())
stones = input()

removal_count = 0

for i in range(1, n):
    if stones[i] == stones[i - 1]:
        removal_count += 1

print(removal_count)

