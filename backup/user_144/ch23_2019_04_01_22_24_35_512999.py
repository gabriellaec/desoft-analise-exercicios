def verifica_idade(idade):
    if idade >= 21:
        return('Liberado EUA e BR') 
	elif idade >=18: 
		return 'Liberado BR'
	else:
    	return 'Nao esta liberado'
    
