individual_words = {}
text = input("Text: ")
words = text.split()
for word in words:
        occurrences = individual_words.get(word, 0)
        individual_words[word] = occurrences + 1
words = list(individual_words.keys())
max_length = max((len(word) for word in words))
words.sort()
for word in words:
    print("{:{}} : {}".format(word, max_length, individual_words[word]))