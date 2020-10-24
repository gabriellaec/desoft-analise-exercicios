def verifica_preço(N, lista1, lista2)
if N in lista1:
    x = lista1[N]
    if x in lista2:
        resultado = lista2[x]
    return resultado