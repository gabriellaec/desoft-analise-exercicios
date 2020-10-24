def classifica_idade(x):
	if x <= 11:
		return 'Crianca'
	if 12<=x<=17:
		return 'Adolecente'
	if x>=18:
		return 'Adulto'
print(idade(10))
print(idade(12))
print(idade(21))