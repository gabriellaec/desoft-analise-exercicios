def interseccao_valores(dict1,dict2):
    lista=[]
    for v in dict1:
        for t in dict2:
            if dict1[v]==dict2[t]:
            	lista.append(v)
    return lista