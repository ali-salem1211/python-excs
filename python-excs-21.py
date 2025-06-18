def reverse_words(sentence):
    words = sentence.strip().split()
    return ' '.join(reversed(words))

print(reverse_words("The quick brown fox jumps over the lazy dog"))
