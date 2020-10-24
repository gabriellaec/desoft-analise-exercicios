def eh_crescente(l):
    i = 1
    crescente = True
    while i < len(l):
        if l[i] >= l[i-1]:
            crescente = True
        else:
            crescente = False
            break
        i += 1
    
    return crescente