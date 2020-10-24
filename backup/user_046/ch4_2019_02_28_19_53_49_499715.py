def classifica_idade(idade):
    if idade<=11:
        return 'crianca'
    elif idade>12 and idade<=17:
    	return 'adolescente'
    elif idade>18:
    	return'adulto'
g=classifica_idade(5)
print(g)
u=classifica_idade(12)
print(u)
	