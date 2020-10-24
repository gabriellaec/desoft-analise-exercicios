def remove_vogais(p):
    i = 0
    while i<len(p):
        if l[i] == 'A':
            del(p[i])
        elif l[i] == 'E':
            del(p[i])
        elif l[i] == 'I':
            del(p[i])
        elif l[i] == 'O':
            del(p[i])
        elif l[i] == 'U':
            del(p[i])
        else:
            return p
        i += 1
            