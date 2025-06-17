def find_maximum(numbers):
    if not numbers:
        return "List is empty"
    
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value

# Example usage
my_list = [4, 9, 2, 15, 7]
print("The largest number is:", find_maximum(my_list))
