def lista_sufixos(palavra):
    a = 0
    b = len(palavra)
    lista = []
    while a < b:
        lista.append(palavra[a:b])
        a += 1
    return lista