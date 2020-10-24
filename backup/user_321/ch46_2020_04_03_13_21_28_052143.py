def numero_no_indice(l):
    i = 0
    retorno = []
    while i <= len(l)-1:
        if l[i] == i:
            retorno.append(i)
            i +=1
        else:
            i +=1
    return retorno