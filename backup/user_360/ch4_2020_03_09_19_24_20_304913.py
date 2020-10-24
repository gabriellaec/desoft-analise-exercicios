def classifica_idade(i):
	if int(idade<=11):
		return "crianca"
	elif int(idade>=12) and int(idade<=17):
		return "adolescente"
	else  int(idade>=18):
		return "adulto"        