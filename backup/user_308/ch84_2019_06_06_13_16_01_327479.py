def inverte_dicionario(idades):
    dicn={}
	for nome,idade in idades.items():
    	if idade not in dicn:
        	dicn[idade]=[nome] 
        else:
            dicn[idade]=dicn[idade].append(nome)
    return dicn
             

