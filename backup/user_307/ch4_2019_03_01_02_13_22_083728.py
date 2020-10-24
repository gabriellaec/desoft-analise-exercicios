a=6

def classifica_idade(a):
	if a<=11:
		return 'crianca'
	elif 11<a<18:
		return 'adolescente'
	else:
		return 'adulto'
print (classifica_idade(a))