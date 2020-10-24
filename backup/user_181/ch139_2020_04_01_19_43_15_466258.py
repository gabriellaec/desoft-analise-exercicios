def arcotangente(x,n):
    lista = []
    cont1 = 1
    while cont1 <= (n*2):
        a = (x**cont1)/cont1
        lista.append(a)
        cont1 += 2
    cont2 = 2
    while cont2 <= len(lista):
        b = lista[cont2-2] - lista[cont2-1] + lista[cont2]
        cont2 += 3
    return b