def classifica_idade(idade):
    if idade <= 11: 
    	y = "crianca"
    elif idade >= 12 and idade <= 17:
    	y = "adolescente"
    else:
        y = "adulto"
    return y