def primeiras_ocorrencias(fuka):
	dic = {}
	s = 0
	for i in fuka:
		if i not in dic:
			dic[i] = s
		s += 1
	return dic
            
        