def classifica_idade(n):
    if n <= 11:
        return str('crianca')
    elif n >= 12 and n < 17:
        return str('adolescente')
    else:
        return str('adulto')
    
print (classifica_idade(18))