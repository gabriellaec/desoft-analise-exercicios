def aniversariantes_de_setembro(dic1):
    dic2={}
    for i in dic1:
        nome = dic1[i]
        for a in nome:
            data = nome[a]
            for b in data:
                if data[4] == '9':
                    dic2 += nome
	return dic2