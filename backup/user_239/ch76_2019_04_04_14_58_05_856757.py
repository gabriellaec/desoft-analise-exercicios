def aniversariantes_de_setembro(dic)
	nomes={}
    for k,v in dic.items():
        if v[3:4]=='09':
            nomes[k]=v