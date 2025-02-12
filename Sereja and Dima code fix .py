n = int(input())
cards = list(map(int, input().split()))

sereja_points = 0
dima_points = 0

while len(cards) > 0:
    if cards[0] > cards[-1]:
        if n % 2 == 0:
            sereja_points += cards.pop(0)
        else:
            dima_points += cards.pop(0)
    else:
        if n % 2 == 0:
            sereja_points += cards.pop(-1)
        else:
            dima_points += cards.pop(-1)

print(sereja_points, dima_points)
