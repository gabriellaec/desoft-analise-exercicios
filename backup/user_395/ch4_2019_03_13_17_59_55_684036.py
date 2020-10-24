def classifica_idade(i):
    if i>=18:
        return ('adulto')
    elif i>=12:
        return ('adolescente')
    else:
        return ('crianca')
print (classifica_idade(7))
print (classifica_idade(16))
print (classifica_idade(21))