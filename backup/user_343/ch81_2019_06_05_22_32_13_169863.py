def interseccao_valores(dic1, dic2):
    lista=[]
    for v in dic1.values():
    	for k in dic2.values():
        	if v==k:
            	lista.append(v)
	return lista