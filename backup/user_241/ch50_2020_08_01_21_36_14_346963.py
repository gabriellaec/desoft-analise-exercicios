def junta_nome_sobrenome(lista1,lista2):
    lista = []
    i = 0
    while i < len(lista1):
        x = lista1[i] + ' ' + lista2[i]
        lista.append(x)
        i += 1
    return lista