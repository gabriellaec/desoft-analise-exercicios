def filtra_positivos(lista):
    listapos = [] 
    for numero in lista:
        if numero > 0:
            listapos.append(numero)
    return listapos