def classifica_idade(idade):
    if (0<=idade<=11):
        return('crianca')
    elif (12<=idade<=17):
        return('adolescente')
    elif (idade<=18):
        return('adulto')
    elif (idade<0):
        return('idade não válida')

idade = 6

print(classifica_idade(idade))
