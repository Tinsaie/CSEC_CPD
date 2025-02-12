matrix = []
for i in range(5):
    row = []
    line = input()
    for char in line:
        if char != ' ':
            row.append(int(char))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            moves = abs(i - 2) + abs(j - 2)
            print(moves)
            break
