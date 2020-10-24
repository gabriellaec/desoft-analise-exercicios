def aniversariantes_de_setembro(dic1):
    dic2={}
    for nome in dic1:
        if dic1[nome][4] == '9':
            dic2[nome] = dic1[nome]
	return dic2