def word_count(sentence):
    words = sentence.lower().split()
    count = {}
    for word in words:
        word = word.strip('.,!?')
        count[word] = count.get(word, 0) + 1
    return count

sentence = "Hello world! Hello again, world."
print(word_count(sentence))
