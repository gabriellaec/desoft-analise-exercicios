def classifica_idade(a) :
	a=int(input('idade: '))
	if a <= 11:
		print('crianca')
	elif 12>=a<=17:
		print('adolescente')
	elif a>=18:
		print('adulto')
	return (classifica_idade(a))