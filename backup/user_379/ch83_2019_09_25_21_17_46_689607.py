def medias_por_inicial(dic):
    resp={}
    for i in dic.keys():
        if i[0] in resp:
            resp[i[0]].append(dic[i])
        else:
            resp[i[0]]=[dic[i]]
	for i in resp.keys():
        comp = len(resp[i])
 		soma=0
        for j in range (len(resp[i])):
			soma+=resp[i][j]
		m=soma/comp
        resp[i]=m
	return resp