k, r = map(int, input().split())

# Try buying from 1 to 10 shovels
for shovels in range(1, 11):
    total_price = k * shovels
    if total_price % 10 == 0 or total_price % 10 == r:
        print(shovels)
        break

