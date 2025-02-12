s1, s2, s3, s4 = map(int, input().split())

# Count the number of distinct colors
distinct_colors = len(set([s1, s2, s3, s4]))

# The number of horseshoes to buy is 4 minus the number of distinct colors
print(4 - distinct_colors)
