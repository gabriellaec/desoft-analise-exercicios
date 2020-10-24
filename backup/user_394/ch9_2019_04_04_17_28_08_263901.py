def lista_sufixos (palavra):
    lista = []
    i = 0
    while i < len(palavra):
        lista.append(palavra)
        i += 1
    return lista_sufixos