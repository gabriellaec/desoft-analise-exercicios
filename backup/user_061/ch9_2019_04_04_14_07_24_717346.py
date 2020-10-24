def lista_de_sufixos(string):
    lista = []
    i = len(string) - 1
    soma = ''
    while i >= 0:
        soma += string[i]
        lista.append(soma)
        i -= 1
    return lista