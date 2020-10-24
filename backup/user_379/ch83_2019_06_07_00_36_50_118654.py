def medias_por_inicial(dic):
    nomes=get_keys(dic)
    d={}
    for i in nomes:
        if not d.has_key(i[0]):
            d[i[0]]=dic[i]
        else:
            d[i[0]] = (d[i[0]]+dic[i])/2
    return d
    
    
def get_keys(dic):
    l=[]
    for i in dic.keys():
        l.append(i)
	return l