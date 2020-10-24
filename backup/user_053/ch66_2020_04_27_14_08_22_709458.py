def lista_sufixos(palavra):
    lista = []
    for i in range (0, len(palavra) - 1):
        sufixo = palavra[i: ]
        lista.append(sufixo)
    return lista