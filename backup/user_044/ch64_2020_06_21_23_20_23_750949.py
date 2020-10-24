def acha_bigramas(string):
    i = 0
    ls = []
    while i<len(string)-1:
        if (string[i]+string[i+1]) not in ls:
            ls.append(string[i]+string[i+1])
        i += 1
    return ls