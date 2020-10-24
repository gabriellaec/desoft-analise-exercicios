def interseccao_valores(dic1,dic2):
    lista=[]
    for k,v in dic1.items():
        if v in dic2:
            lista.append(v)
	return lista
