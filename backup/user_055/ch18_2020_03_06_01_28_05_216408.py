def verifica_idade(idade):
    if 17 < idade < 21:
        print('Liberado BRASIL')
    if idade >= 21:
        print('Liberado EUA e BRASIL')
    if idade < 18:
        print('Não está liberado')