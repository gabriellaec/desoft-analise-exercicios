def classifica_idada(idade):
    if idade<=11:
		x='crianca'
    elif 12<=idade<=17:	
		x='adolescente'
	else:
		x='adulto'
        return x
print(classifica_idade(idade))
    