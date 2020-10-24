def monta_dicionario(lista1, lista2):
    saida = {}
    i = 0
    while i < len(lista2):   
        for e in lista1:
            saida[e] = lista2[i]
            i+=1
    return saida
