def junta_listas(lista_composta):
    lista_simples = []
    i = 0
    while i < len(lista_composta):
        z = 0
        while z < len(lista_composta[i]):
            if lista_composta[i][z] not in lista_simples:
                lista_simples.append(lista_composta[i][z])
            z += 1
        i += 1
    return lista_simples
