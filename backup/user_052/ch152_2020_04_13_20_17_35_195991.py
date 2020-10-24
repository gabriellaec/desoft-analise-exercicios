def verifica_preço(xx,lista1,lista2):
    if xx in lista1:
        x = lista1[xx]
        if x in lista2:
            resultado = lista2[x]
        return resultado