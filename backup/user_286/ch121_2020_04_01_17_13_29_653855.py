def subtracao_de_listas (lista1, lista2):
    
    lista_final = []
    
    for item1 in lista1:
        contador = 0
        for item2 in lista2:
            if item1 == item2:
                contador += 1
        if contador == 0:
            lista_final.append(item1)

    return lista_final