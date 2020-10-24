def arcotangente(x,n):
    lista = []
    cont1 = 1
    while cont <= (n*2):
        a = (x**cont)/cont
        lista.append(a)
        cont += 2
    cont2 = 2
    while cont <= len(lista):
        b = lista[cont-2] - lista[cont-1] + lista[cont]
        cont += 3
    return b