def classifica_idade(x):
    if x>=11:
        return ('crianca')
    elif x>=18:
        return ('adulto')
    else:
        return ('adolescente')
print (classifica_idade(6))
print (classifica_idade(21))
print (classifica_idade(16))