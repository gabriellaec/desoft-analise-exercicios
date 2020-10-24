def inverte_dicionario(dicionario):
    dic={}
    lista_vazia=[]
    for k,v in dicionario.items():
    	if k not in dic:
            dic[v] = [k]
        else:
            dic[i].append(k)
    return dic