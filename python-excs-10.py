def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

# Example usage
word = "programming"
letter = "m"
print(f"The letter '{letter}' appears {count_letter(word, letter)} times in '{word}'.")
