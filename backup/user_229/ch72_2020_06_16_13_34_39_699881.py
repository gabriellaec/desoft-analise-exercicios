def lista_caracteres(string):
    lista = []
    for letra in string:
        if letra not in lista:
            lista.append(''.format(letra))
    return lista