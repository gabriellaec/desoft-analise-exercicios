def verifica_idade(i):
	if i>=21:
		return ('maior de idade no EUA e no BR')
	elif i>=18:
		return('maior de idade no BR')
	else:
		return('voce se ferrou')
    
print(testa_idade(4))