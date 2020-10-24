def classifica_idade(numero):
	if numero <= 11:
		return "crianca"
	elif numero >= 18:
		return "adulto"
	else:
		return "adolescente"
a = int(input("Digite a idade"))