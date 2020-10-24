def lista_caracteres(palavra):
    lista=[]
    i=0
    while i<len(palavra):
        letra=palavra[i]
        if letra in lista:
            lista=lista
        else:
            lista.append(letra)
        i=i+1
    return lista