def remove_vogais(word):
    new = ''
    i = 0
    while i < len(word):
        m = word[i]
        if m != 'a' and m !='e' and m !='i' and m !='o' and m !='u':
            new += word[i]
        i += 1
    return new