def remove_vogais(p):
    i = 0
    while i<len(p):
        if p[i] == 'a':
            del(p[i])
        elif p[i] == 'e':
            del(p[i])
        elif p[i] == 'i':
            del(p[i])
        elif p[i] == 'o':
            del(p[i])
        elif p[i] == 'u':
            del(p[i])
        else:
            return p
        i += 1
            