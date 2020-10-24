def estritamente_crescente(lista):
    
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l