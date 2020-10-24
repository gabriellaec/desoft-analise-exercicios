def lista_sufixos(string):
    lista = []
    i = len(string)-1
    soma = ''
    while i >= 0:
        soma += string[i]
        lista.append(soma[::-1])
        i -= 1
    return lista