def junta_listas(lista_composta):
    lista_simples = []
    t = 0
    while t < len(lista_composta):
        if type(lista_composta[t]) == list:
            i = 0
            while i < len(lista_composta[t]):
                lista_simples.append(lista_composta[t][i])
                i += 1
        if type(lista_composta[t]) != list:
            lista_simples.append(lista_composta[t])
        t += 1
    return lista_simples