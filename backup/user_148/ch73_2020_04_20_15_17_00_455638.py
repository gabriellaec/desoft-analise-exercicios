def remove_vogais(p):
    i = 0
    while i<len(p):
        if p[i] == 'A':
            del(p[i])
        elif p[i] == 'E':
            del(p[i])
        elif p[i] == 'I':
            del(p[i])
        elif p[i] == 'O':
            del(p[i])
        elif p[i] == 'U':
            del(p[i])
        else:
            return p
        i += 1
            