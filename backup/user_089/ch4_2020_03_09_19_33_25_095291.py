def classifica_idade(i):
    
    if i <= 11:
        return('crianca')

    if i >= 12 and i <= 17 :
        return ("adolescente")

    else :
        return ('adulto')
print(classifica_idade(i))