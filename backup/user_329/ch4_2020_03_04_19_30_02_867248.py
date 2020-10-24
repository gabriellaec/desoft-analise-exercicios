
def classifica_idade(idade):
    
	if idade<=11:
        resultado = "crianca"

	elif 11<idade<18:
        resultado = "adolescente"
        
	elif idade>=18:
        resultado = "adulto"
    
    return resultado