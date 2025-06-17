def count_words(sentence):
    words = sentence.split()
    return len(words)

# Example usage
sentence = input("Enter a sentence: ")
print("Word count:", count_words(sentence))
