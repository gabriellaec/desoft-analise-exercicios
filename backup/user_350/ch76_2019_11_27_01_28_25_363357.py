def aniversariantes_de_setembro(dic):
    dicionario = {}
	for k,v in dic.items():
        if v[3] == 0 and v[4] == 9:
            dicionario[k] = v
    return dicionario