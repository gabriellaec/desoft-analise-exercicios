def classifica_idade(x):
    if x<11:
        return ('crianca')
    elif x<17 and x>12:
        return ('adolescente')
    else:
        return ('adulto')
print (classifica_idade(x))    