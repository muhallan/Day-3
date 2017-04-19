def wordcount(words):
    """ get the number of occurrences of words in a given sentence """
    if not isinstance(words, str):
        raise TypeError("not a string type")

    word_counter = dict()

    list_words = words.strip(" \t\n\r\v\f").split()
    for word in list_words:
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1
    return word_counter
