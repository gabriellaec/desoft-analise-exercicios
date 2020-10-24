def lista_caracteres(word):
    i=0
    lista = []
    while i<len(word):
        if word[i] not in lista:
            lista.append(word[i])
        i+=1
    return lista