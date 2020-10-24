def aniversariantes_de_setembro(dicionario):
    ani_setembro = {}
    for n in dicionario.keys():
    	for i in dicionario.values():
        	data = i.split("/")
            if data[1] == '09':
                ani_setembro[n] = i
	return ani_setembro