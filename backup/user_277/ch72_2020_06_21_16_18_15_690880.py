def lista_caracteres(string):
    lista = []
    i = 0
    while i < len(string):
        if i not in lista:
            lista.append(i)
        i+=1
    return(lista)