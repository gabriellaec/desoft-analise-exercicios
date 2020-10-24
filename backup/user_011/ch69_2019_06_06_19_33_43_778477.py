def junta_listas(lista_listas):
    unica = []
    i = 0
    j = 0
    while i < len(lista_listas):
        if len(lista_listas[i][i]) > 1:
            unica.append(lista_listas[i][j])
            j += 1
        else:
            unica.append(lista_listas[i][i])
        i += 1
        return unica