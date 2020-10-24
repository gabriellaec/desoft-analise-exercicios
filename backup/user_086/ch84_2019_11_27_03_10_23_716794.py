def inverte_dicionario(dic):
    novo_dic = {}
    t = 0
    while t<len(dic.values()):
    	for i in dic[t]:
            if not i in novo_dic:
                novo_dic[i] = dic[t]
    t+=1 
    return novo_dic