def interseccao_chaves(dic0,dic2):
	chaves=[]
	for l in dic0.keys():
		if l in dic2:
		chaves.append(l)
	return chaves