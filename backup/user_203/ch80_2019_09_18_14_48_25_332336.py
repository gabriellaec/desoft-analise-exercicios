def interseccao_chaves(dict1,dict2): 
	lista=[]
	for x in dict1.keys(): 
		if x in dict2.keys(): 
			lista.append(x) 
	return lista 