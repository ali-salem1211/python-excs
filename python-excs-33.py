# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Numbers that appear in both sets (intersection)
common = set1 & set2

# Numbers that appear in only one set (symmetric difference)
unique = set1 ^ set2

print("Common numbers:", common)
print("Numbers in only one set:", unique)
