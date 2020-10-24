def classifica_idade (idade):
    if idade <=11:
        return('Crianca')
    elif idade <=17:
            return('adolescente')
    else:
        return('Adulto')
print(classifica_idade(10))
print(classifica_idade(15))
print(classifica_idade(56))
