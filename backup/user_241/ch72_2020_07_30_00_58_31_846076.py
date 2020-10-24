def lista_caracteres(x):
    lista = []
    for caractere in x:
        if caractere not in lista:
            lista.append(caractere)
    return lista