verifica_idade = int('Qual a sua idade?')
if  verifica_idade >= 21:
    print ('Liberado EUA e BRASIL')
elif verifica_idade >= 18 and verifica_idade < 21:
    print('Liberado BRASIL')
else:
    print ('Não está liberado')
