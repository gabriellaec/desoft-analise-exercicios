def inverte_dicionario(dicionario):
    dic={}
    lista_vazia=[]
    for k,v in dicionario.items():
        dic[v] = k
        for m,n in dicionario.items():
            if n == v:
            	lista_vazia.append(v)
            dic[n] = lista_vazia
	return dic