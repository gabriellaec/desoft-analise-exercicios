def zera_negativos(lista):
    lista_novo = []
    for i in lista:
        if i < 0:
            lista_novo.append(0)
    return lista_novo 
