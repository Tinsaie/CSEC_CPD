s = input()

uppercase_count = sum(1 for char in s if char.isupper())
lowercase_count = len(s) - uppercase_count

if uppercase_count > lowercase_count:
    print(s.upper())
else:
    print(s.lower())
