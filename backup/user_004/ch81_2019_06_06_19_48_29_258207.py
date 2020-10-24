def interseccao_valores(dic, dic1):
    lista=[]
    for k in dic.values():
        if k not in lista:
            lista.append(k)
    for k in dic1.values():
        if k not in lista:
            lista.append(k)
	return lista