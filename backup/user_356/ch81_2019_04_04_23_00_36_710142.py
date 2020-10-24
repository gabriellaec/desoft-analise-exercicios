def interseccao_valores(dict1, dict2):
    lista=[]
    for e in dict1.values():
    	for i in dict2.values():
        	if i==e:
                lista.append(e)
    return lista