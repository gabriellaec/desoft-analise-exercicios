i = int(input("insira sua idade"))

def classifica_idade(x):
    if 0<x<=11:
        print("crianca")
    elif 11<x<=17:
      	print("adulto")
    elif 17<x:
        print("Adulto")
        
conclusão = classifica_idade(i)
print (conclusão)