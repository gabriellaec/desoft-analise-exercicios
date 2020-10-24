def aniversariantes_de_setembro(dicio):
	setembro = {}
    nomes = []
    datas = []
    for n,d in dicio.items():
        nomes.append(n)
        datas.append(d)
    for i in datas:
        if datas[i][3:5] == '09':
            setembro[nomes[i]] = datas[i]
	return setembro