def junta_listas(lista_composta):
    contador = 1
    lista_final = []
    lista_final.append(lista_composta[0])
    while contador < len(lista_composta):
        lista_final[0] += lista_composta[contador]
        contador += 1
    return lista_final