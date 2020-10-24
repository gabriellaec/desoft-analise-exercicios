def conta_letras(s):
	lista = list(s)
	dic = {}
	for e in lista:
		if e in dic:
			dic[e]+=1
		else: 
			dic[e] = 1
	return dic