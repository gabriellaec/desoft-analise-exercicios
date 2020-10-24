def verifica_idade(idade):
    h= "Não esta liberado"
    z= "Liberado BRASIL"
    x= "Liberado EUA e BRASIL"
	if idade > 21:
    	return x
    elif > 18:
        return z
    else:
        return h
print(verifica_idade(idade))