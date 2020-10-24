def traduz (lista_ing, dic):
    lista_port = []
    i = 0
    while i < len(lista_ing):
        for c, v in dic.items():
            if c == lista_ing[i]:
                lista_port.append(v)
        i += 1
    return lista_port