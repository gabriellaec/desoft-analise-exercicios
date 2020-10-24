def inverte_dicionario(dicionario):
	dic={}
	for k,v in dicionario.items():
		if k not in dic:
			dic[v] = [k]
		else:
			dic[i].append(k)
	return dic