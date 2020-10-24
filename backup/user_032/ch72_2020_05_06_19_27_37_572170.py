def lista_caracteres(palavra):
    lista = list(palavra)
    lista2 = []
    for letra in lista:
        if letra not in lista2:
            lista2.append(letra)
    return lista2