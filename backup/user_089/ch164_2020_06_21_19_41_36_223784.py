def traduz(lista, dicionario):
    lista_port = []
    for e in lista:
        for k,v in dicionario.items():
            if e == k:
                lista_port.append(v)
    return lista_port