def monta_dicionario(lis1, lis2):
    dic = {}
    for a in lis1:
        dic = lis1[a]
	for b in lis2:
        dic[a] = lis2[b]
	return dic