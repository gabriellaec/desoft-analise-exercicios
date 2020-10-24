def classifica_idade(n):
    if n <= 11:
        return str('crianca')
    elif 12 < n < 17:
        return str('adolescente')
    elif n > 17:
        return str('adulto')
    
print classifica_idade(18)