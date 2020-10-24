def lista_caracteres(palavra):
    lista = []
    for i in palavra:
        if i not in palavra:
            lista.append(i)
    return lista