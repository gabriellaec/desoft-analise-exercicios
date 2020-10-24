def estritamente_crescente(x):
    lista = []
    h = x[0]
    lista.append(h)
    for e in x:
        y = 1
        número = lista[y]
        if e > número:
            lista.append(e)
            y += 1
        else:
            y +=1
    return lista