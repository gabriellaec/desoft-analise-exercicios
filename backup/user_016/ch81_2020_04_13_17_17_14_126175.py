def interseccao_valores(dicionario1,dicionario2):
    lista = []
    for i in dicionario1.values():
        if i in dicionario2.values():
            lista.append(i)
    return lista