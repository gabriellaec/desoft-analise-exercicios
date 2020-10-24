def traduz(lista, dicionario):
    lista_port = []
    for k,v in dicionario.items():
        for e in lista:
            if e == k:
                lista_port.append(v)
    return lista_port