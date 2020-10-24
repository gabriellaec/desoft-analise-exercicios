def conta_ocorrencias(l):
    dic = {}
    for i in l:
        if not i in dic :
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

def conta_letras(p):
    lista_p = []
    for i in p:
        lista_p.append(i)
    palavras_e_números = conta_ocorrencias(lista_p)
    return palavras_e_números