def interseccao_chaves(d1,d2):
    lista=[]
    for e in d1.keys():
        for i in d2.keys():
	        if e==i:
                	lista.append(e)
    return lista