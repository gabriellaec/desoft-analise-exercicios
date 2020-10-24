def traduz(lista_e,dic):
    lista_p = []
    for eng in lista_e:
        port = dic[eng]
        lista_p.append(port)
    return lista_p