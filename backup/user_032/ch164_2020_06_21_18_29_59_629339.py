def traduz(lista_palavras, eng2port):
    lista = []
    for x in lista_palavras:
        for c,v in eng2port.items():
            if x==c:
                lista.append(v)
    return lista
    