def lista_sufixos (string):
    lista = []
    i = 0
    while i < len(string):
        sufixo = string[i:]
        lista.append(sufixo)
        i = i + 1
    return lista