def classifica_idade(idade):
    if idade <= 11:
        return "crianca"
  	elif idade >= 12 or idade <=17:
        return "adolescente"
    elif idade > 18:
        return "adulto"
        