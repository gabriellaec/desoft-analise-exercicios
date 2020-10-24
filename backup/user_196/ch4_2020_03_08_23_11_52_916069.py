def classifica_idade(a):
    if a <= 11:
        return "crianca"
	elif a >= 12 and a <= 17:
        return "adolescente"
	else:
        return "adulto"

b = int (input ("Digite a sua idade:"))
print (classifica_idade(b))
