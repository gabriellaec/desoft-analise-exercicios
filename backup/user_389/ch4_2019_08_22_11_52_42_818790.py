def classifica_idade(idade):
    
    if idade <= 11:
        x='crianca'
        return x
    elif idade >= 12 and idade <= 17:
        x='adolescente'
        return x
    else:
        x='adulto'
        return x
        
x=classifica_idade(15)
print(x)

    
        