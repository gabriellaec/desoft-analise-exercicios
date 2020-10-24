def remove_vogais(p):
    l = []
    i = 0
    
    while i<len(p):
        if p[i] != 'a' or 'e' or 'i' or 'o' or 'u':
            l.append(p[i])
        i += 1
        
    return l
