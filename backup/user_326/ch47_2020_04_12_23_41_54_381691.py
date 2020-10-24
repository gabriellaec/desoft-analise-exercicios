def estritamente_crescente(lista):
    lista_crescente = []
    maior_valor = 0
    print(lista)
    if not lista:
        return lista
    else:  
        for i in lista:           
            if lista[i] > maior_valor:
                lista_crescente.append(lista[i])
                maior_valor = lista[i]
    print(lista)
    print(lista_crescente)
    return lista_crescente
