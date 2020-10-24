def classifica_idade(idade):
    if (0<=idade<=11):
        print('crianca')
    elif (12<=idade<=17):
        print('adolescente')
    elif (idade<=18):
        print('adulto')
    elif (idade<0):
        print ('idade não válida')

idade = 6

print(classifica_idade(idade))
