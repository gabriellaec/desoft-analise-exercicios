def classifica_idade(jaca):
	if jaca<=11:
		return "crianca"
	if jaca>=12 and jaca<=17:
		return "adolescente"
	if jaca>=18:
		return "adulto"