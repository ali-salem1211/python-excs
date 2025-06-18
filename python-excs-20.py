def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in sentence if char in vowels)

print(count_vowels("Hello, how are you doing today?"))