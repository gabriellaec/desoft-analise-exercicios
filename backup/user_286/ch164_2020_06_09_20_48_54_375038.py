def traduz(lista_eng, dic_tradutor):
    lista_port = []
    for palavra in lista_eng:
        lista_port.append(dic_tradutor[palavra])

    return lista_port