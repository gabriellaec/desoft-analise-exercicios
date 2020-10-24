def inverte_dicionario(dicionario):
	dic={}
	for k,v in dicionario.items():
		if v not in dic:
			dic[v] = [k]
		else:
			dic[v].append(k)
	return dic