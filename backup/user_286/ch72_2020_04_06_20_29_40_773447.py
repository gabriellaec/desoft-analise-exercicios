def lista_caracteres(frase):
    lista = []
    for letra in frase:
        if letra not in lista:
            lista.append(letra)
        

    return lista