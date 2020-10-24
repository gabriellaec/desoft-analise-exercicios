def zera_negativos(lista):
    lista_novo = []
    for i in lista:
        if i < 0:
            i = 0
    return lista_novo 
