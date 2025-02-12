n = int(input())
birds_on_wires = list(map(int, input().split()))
m = int(input())

# Process each shot
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1  # Convert to 0-based index
    y -= 1  # Convert to 0-based index
    
    # Birds to the left of the shot jump up to the previous wire
    if x > 0:
        birds_on_wires[x - 1] += y
    
    # Birds to the right of the shot jump down to the next wire
    if x < n - 1:
        birds_on_wires[x + 1] += birds_on_wires[x] - y - 1
    
    # After the shot, the wire is empty at the shot position
    birds_on_wires[x] = 0

# Output the number of birds left on each wire
for birds in birds_on_wires:
    print(birds)
