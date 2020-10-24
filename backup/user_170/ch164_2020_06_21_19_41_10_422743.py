def traduz(lista, dicionario):
    traducoes = []
    for i in lista:
        if i in dicionario:
            traducoes.append(dicionario[i])
    return traducoes