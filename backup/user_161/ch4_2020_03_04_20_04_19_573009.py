def classifica_idade(jaca):
	if jaca<=11:
		return "crianca"
	elif jaca>=12 and jaca<=17:
		return "adolescente"
	else: # jaca>=18
		return "adulto"
