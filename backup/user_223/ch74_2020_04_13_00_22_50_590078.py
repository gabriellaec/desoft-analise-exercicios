def conta_bigramas(s):
	dic = {}
	lista=list(s)
	lista_bi = []
	for i in range (len(lista)-1):
		bi = lista[i] + lista[i+1]
		lista_bi.append(bi)
	for e in lista_bi:
		if e in dic:
			dic[e]+=1
		else:
			dic[e]=1
	return dic