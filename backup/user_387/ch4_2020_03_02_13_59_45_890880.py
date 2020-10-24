def classifica_idade(x):
    if x <= 11:
        return('crianca')

    elif x <= 17:
        return('adolescente')

    else: 
        return('adulto')

x = float(input("Qual sua idade: "))

c = classifica_idade(x)

print(c)

    
    
    

