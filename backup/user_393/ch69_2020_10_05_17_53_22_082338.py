def junta_listas(lista):
    lista_completa= []
    i= 0
    while i < len(lista):
        x= 0
        while x < len(lista[i]):
            lista_completa.appen(lista[i][x])
            x= x + 1
        i= i + 1
    return lista_completa