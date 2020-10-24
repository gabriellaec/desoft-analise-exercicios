
def classifica_idade(i):
    if i<=11:
        return "crianca"
    elif 11<i<=17:
      	return "adolescente"
    elif 17<i:
        return "adulto"
        
i = int(input("insira sua idade"))
conclusão = classifica_idade(i)
print (conclusão)

