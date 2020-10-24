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


def encontra_maximo(matriz):
    t = 1
    matriz_plana = [] 
    matriz_plana = junta_listas(matriz)
    matriz_crescente = [matriz_plana[0]]
    while t < len(matriz_plana):
        if matriz_plana[t] > matriz_crescente[-1]:
            matriz_crescente.append(matriz_plana[t])
        t += 1
    return matriz_crescente[-1]