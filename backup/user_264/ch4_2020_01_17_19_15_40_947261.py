i = int(input("insira sua idade"))

def classifica_idade(x):
    if 0<x<=11:
        return "crianca"
    elif 11<x<=17:
      	return "adolescente"
    elif 17<x:
        return "adulto"
        
conclusão = classifica_idade(i)
print (conclusão)