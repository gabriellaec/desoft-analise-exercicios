def classifica_idade(x):
    if x<11:
    	return ("Criança")
	elif 12<x<17:
        return ("Adolescente")
    else x>18:
        return ("Adulto")
print (classifica_idade(19))
    