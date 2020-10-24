def estritamente_crescente(lista):
    lista_crescente = []
    maior_valor = 0
    for i in lista:
        if not len(lista):
            return lista           
        elif lista[i] > maior_valor:
            lista_crescente.append(lista[i])
            maior_valor = lista[i]
    print(lista)
    print(lista_crescente)
    return lista_crescente

