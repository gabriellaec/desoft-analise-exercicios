def medias_por_inicial(dic = {}):
	dic_novo = {}
    for i in dic:
        if i[0] not in dic_novo:
            sum = 0
            cont = 0
            for j in dic:
                if j[0] == i[0]:
                    sum += dic[j]
                    cont += 1
            dic_novo[i[0]] = sum/cont
  	return dic_novo