def interseccao_chaves(dic0,dic2):
	chaves=[]
	for k1 in dic0.keys():
		if k1 in dic2:
            chaves.append(k1)
	return chaves