def junta_listas(lista_composta):
    lista_simples = []
    for sublistas in lista_composta:
        for numeros in sublistas:
            lista_simples.append(numeros)        
    return lista_simples