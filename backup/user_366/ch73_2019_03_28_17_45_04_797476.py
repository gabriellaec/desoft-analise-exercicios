def remove_vogais(word):
    new = []
    i = 0
    while i < len(word):
        m = word[i]
        if m != 'a' or 'e' or 'i' or 'o' or 'u':
            new.append(m)
        i += 1
    return new