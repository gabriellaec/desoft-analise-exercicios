def primeiras_ocorrencias(word):
    d = {}
    i = 0
    print(len(word))
    while i < len(word):
        if word[i] in d:
            pass
        else:
            d[word[i]] = i
        i += 1
    return d