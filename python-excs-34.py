# Sort a list of names by length
names = ["Alice", "Bob", "Christina", "Dave"]
sorted_names = sorted(names, key=lambda name: len(name))
print("Names sorted by length:", sorted_names)

# Filter to keep only positive numbers
numbers = [-5, 3, 0, -2, 8, 1]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print("Positive numbers:", positive_numbers)
