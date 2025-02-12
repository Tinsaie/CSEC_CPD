n = int(input())
solvable_count = 0

for _ in range(n):
    petya = int(input())
    vasya = int(input())
    tonya = int(input())
    
    if petya + vasya + tonya >= 2:
        solvable_count += 1

print(solvable_count)
