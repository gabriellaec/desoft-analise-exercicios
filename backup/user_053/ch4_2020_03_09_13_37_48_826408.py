classifica_idade=int(input('Digite a sua idade: '))

if classifica_idade<=11:
    print('crianca')
elif classifica_idade>11 and classifica_idade<=17:
    print('adolescente')
else:
    print('adulto')