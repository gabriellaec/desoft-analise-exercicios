def traduz (lista_ing, dicionario):
    lista_port = []
    for palavra_ing in lista_ing:
        for port, eng in dicionario.items():
            if palavra_ing == eng:
                lista_port.append(port)
    return lista_port