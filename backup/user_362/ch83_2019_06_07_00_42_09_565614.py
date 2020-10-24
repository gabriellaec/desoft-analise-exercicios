def medias_por_inicial(dict_notas):
    entrada={}
    for k,v in dict_notas.items():
        entrada[k[0]]= v
        for m,n in dict_notas.items():
            if k[0] == m[0] and k!= m:
                entrada[k[0]] += (n-v)/2
	return entrada