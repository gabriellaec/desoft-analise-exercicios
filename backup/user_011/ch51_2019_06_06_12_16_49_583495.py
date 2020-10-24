def estritamente_crescente(lista_num):
    lista_crescente = []
    i = 0
    while i < len(lista_num):
        a = lista_num[i+1]
        b = lista_num[i]
        if a > b:
            lista_crescente.append(a)
    return lista_crescente
