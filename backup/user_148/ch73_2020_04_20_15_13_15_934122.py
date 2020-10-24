def remove_vogais(p):
    l = []
    i = 0
    while i<len(p):
        if l[i] != 'A' or 'E' or 'I' or 'O' or 'U':
            l.append(l[i])
        i += 1
        
    return l
            