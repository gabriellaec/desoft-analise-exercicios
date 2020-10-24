def inverte_dicionario(dicio):
    dic={}
    for k, v in dicio.items():
	    if v in dic.keys():
		    dic[v].append(dicio[k])
	    else:
		    dic[v] = [dicio[k]]
    return dic