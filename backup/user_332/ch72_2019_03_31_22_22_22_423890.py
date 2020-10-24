def lista_caracters(palavra):
    lista = []
    for e in palavra:
        if not e in lista:
            lista.append(e)
    return lista