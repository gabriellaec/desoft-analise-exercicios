def estritamente_crescente(lista):
    l = []
    a = len(lista)
    x = 0
    y = 0
    while x<a:
        if x == 0:
            l.append(lista[x])
            x+=1
        if lista[x] > l[y]:
            l.append(lista[x])
            y+=1
            x+=1
        else:
            x+=1
    return l