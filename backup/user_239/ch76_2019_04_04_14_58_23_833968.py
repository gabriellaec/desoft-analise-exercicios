def aniversariantes_de_setembro(dic)
	nomes={}
    for k,v in dic.items():
        if v[3:5]=='09':
            nomes[k]=v
    return nomes