def numero_no_indice(l):
    i = 0
    retorno = []
    for i in range(len(l)):
        if l[i] == i:
            retorno.append(i)
            i +=1
        else:
            i +=1
    return retorno