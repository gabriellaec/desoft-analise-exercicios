def zera_negativos(lista_inteiros):
    t = 0
    lista_naturais = []
    while t < len(lista_inteiros):
        if lista_inteiros[t] ==0:
            lista_naturais.append(0)
        if lista_inteiros[t] > 0:
            lista_naturais.append(lista_inteiros[t])
        if lista_inteiros[t] < 0:
            lista_naturais.append(0)
        t += 1
    return lista_naturais