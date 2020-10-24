def numero_no_indice(n):
    i = 0
    retorno = []
    while i < len(n):
        if n[i] == i:
            retorno.append(i)
        i += 1
    return retorno



    