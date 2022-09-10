def index_words(words: 'list[str]'):
    indexed_words: 'dict[str,list[str]]' = {}
    for word in words:
        if word[0] not in indexed_words:
            indexed_words[word[0]] = []
        indexed_words[word[0]].append(word)
    return indexed_words

def test():
    words = open("words.txt", "r").read().split("\n")

    print(index_words(words))

test()