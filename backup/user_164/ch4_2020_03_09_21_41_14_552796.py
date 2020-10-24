def classifica_idade(x):
    if x<11:
    	return ("Criança")
	elif x>12:
        return ("Adolescente")
    elif x<17:
        return ("Aldolescente")
    else x>18:
        return ("Adulto")
print (classifica_idade(19))
    