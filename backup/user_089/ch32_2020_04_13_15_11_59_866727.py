def lista_primos(g):
    lista = []
    i = 
    while i < g:
        if i % 2 == 0 and i != 2 or i == 0 or i == 1:
            i = i +2
        if x % i == 0:
            i = i + 2
        else:
            lista.append(i)
        i += 2
    return lista