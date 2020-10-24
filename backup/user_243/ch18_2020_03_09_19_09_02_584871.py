def verifica_idade(idade):
    if idade<18:
        h="não esta liberado"
    elif idade<21:
        h="Liberado BRASIL"
    else:
        h="Liberado EUA e BRASIL"
	return(h)
