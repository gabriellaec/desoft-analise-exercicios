def lista_caracteres(palavra):
    lista = []
    i = 0
    while i < len(palavra):
        caractere = palavra[i]
        if len(lista) == 0:
            lista.append(caractere)
        else:
            if caractere not in lista:
                lista.append(caractere)
        i += 1

    return lista
