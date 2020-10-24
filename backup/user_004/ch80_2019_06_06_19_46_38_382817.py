def interseccao_chaves(dic, dic1):
    lista=[]
    for k in dic.keys():
        if k not in lista:
            lista.append(k)
    for k in dic1.keys():
        if k not in lista:
            lista.append(k)
	return lista
