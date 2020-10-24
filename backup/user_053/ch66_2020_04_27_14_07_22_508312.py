def lista_sufixos(palavra):
    lista = []
    for i in range (0, len(palavra) - 1):
        sufixo = palavra[ i: : -1]
        lista.append(sufixo)
    return lista