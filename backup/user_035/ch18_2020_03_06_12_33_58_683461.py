def verifica_idade(idade):
	if idade<18:
		print("Não está liberado")
	if idade>17 and idade<21:
		print("Liberado BRASIL")
	if idade>20:
		print("Liberado EUA e BRASIL")