def inverte_dicionario(idades):
    dicn={}
	for nome,idade in idades.items():
    	if idade not in dicn:
        	x=[nome] 
        else:
            x=dicn[idade]
            x.append(nome)
        dicn[idade]=x
    return dicn
             

