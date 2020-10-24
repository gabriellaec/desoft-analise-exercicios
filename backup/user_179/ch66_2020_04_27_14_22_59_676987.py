def lista_sufixos (string):
    lista = []
    i = 0
    while i < len(string):
        adicionar = string[i:]
        lista.append(adicionar)
        i = i + 1
    return lista