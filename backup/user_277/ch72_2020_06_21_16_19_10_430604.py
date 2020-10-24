def lista_caracteres(string):
    lista = []
    i = 0
    while i < len(string):
        if string[i] not in lista:
            lista.append(string[i])
        i+=1
    return(lista)