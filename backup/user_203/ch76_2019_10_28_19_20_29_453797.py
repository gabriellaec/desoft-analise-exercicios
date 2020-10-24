def aniversariantes_de_setembro(dicionario): 
    novodict = {} 
    lista_valores = list(dicionario.values()) 
    lista_chaves = list(dicionario.keys())
    i = 0 
    for data in lista_valores: 
		if lista_valores[i][3] == 0 and lista_valores[i][4] == 9: 
            novodict[lista_chaves[i]] = lista_valores[i] 
	return novodict 
            
            
        