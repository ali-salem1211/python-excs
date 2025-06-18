def safe_get(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

my_list = [10, 20, 30]
print(safe_get(my_list, 1))  # Output: 20
print(safe_get(my_list, 5))  # Output: Index out of range.
