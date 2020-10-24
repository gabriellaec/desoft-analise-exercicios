def estritamente_crescente(x):
    lista = []
    for e in x:
        y = 0
        número = lista[y]
        if e > número:
            lista.append(e)
            y += 1
        else:
            y +=1