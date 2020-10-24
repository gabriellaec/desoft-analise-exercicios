def inverte_dicionario(idades):
    dicn={}
	for nome,idade in idades.items():
    	if idade not in dicn:
        	dicn[idade]=[nome] 
        else:
            x=dicn[idade].append(nome)
        	dicn[idade]=x
    return dicn
             

