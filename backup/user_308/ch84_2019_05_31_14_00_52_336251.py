def inverte_dicionario(idades):
    dicn={}
	for nome,idade in idades:
    	if idade not in dicn:
        	dicn[idade]==nome
        else:
            x=dicn[idade]
            dicn[idade]="{0}, {1}".format(x,nome)
    return dicn
             

