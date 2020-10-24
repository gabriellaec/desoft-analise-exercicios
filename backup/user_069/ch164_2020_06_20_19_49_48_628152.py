def traduz(lista_eng, eng2port):

    lista_port = []

    for palavra in lista_eng:

        if palavra in eng2port:
            palavra_eng = eng2port[palavra]
            lista_port.append(palavra_eng)

    return lista_port