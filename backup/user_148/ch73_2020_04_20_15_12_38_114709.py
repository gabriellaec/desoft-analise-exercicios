def remove_vogais(p):
    l = []
    i = 0
    while i<len(p):
        if l[i] != 'A', 'E', 'I', 'O', 'U':
            l.append(l[i])
        i += 1
        
    return l
            