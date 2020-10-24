def junta_listas(lista):
    lista_final = []
    for listinhas in lista:
        for elemento in listinhas:
            lista_final.append(elemento)
	lista_final = set(lista_final)
    return lista_final