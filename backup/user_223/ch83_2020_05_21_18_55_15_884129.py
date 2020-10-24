def medias_por_inicial(dic):
    novo_dic = {}
    ocorrencias = {}
    for e in dic.keys():
	    if e[0] in novo_dic.keys():
		    novo_dic[e[0]]+=dic[e]
		    ocorrencias[e[0]]+=1
	    else:
		    novo_dic[e[0]] = dic[e]
		    ocorrencias[e[0]] = 1
    for c, v in novo_dic.items():
	    if c in ocorrencias.keys():
		    novo_dic[c]=v/ocorrencias[c]
    return novo_dic