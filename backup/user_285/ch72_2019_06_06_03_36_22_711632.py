def lista_caracteres(palavra):
    lista=[]
    for letra in palavra:
        if letra not in lista:
            lista.append(letra)
    return lista