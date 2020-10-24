def lista_sufixos (string):
    lista = []
    i = 0
    while i < len(string):
        a = len(string) - i
        adicionar = string[:a]
        lista.append(adicionar)
        i = i + 1
    return lista