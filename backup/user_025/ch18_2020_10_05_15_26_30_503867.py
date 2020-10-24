verifica_idade = int(input('Digite sua idade: '))

if verifica_idade >= 21:
    print('Liberado EUA e BRASIL')
elif verifica_maioridade >= 18:
    print('Liberado BRASIL')
else:
    print('Não está liberado')