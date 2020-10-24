def medias_por_inicial(d):
	dnovo = {}
	for i in d.keys():
		if i[0] not in dnovo.keys():
			lista = []
			for j in d.keys():
				if j[0] == i[0]:
					lista.append(d[j])
			dnovo[i[0]] = sum(lista)/len(lista)
	return dnovo