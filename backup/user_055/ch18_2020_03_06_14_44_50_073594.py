def verifica_idade(idade):
    if idade >= 18 and idade <= 21:
        print('Liberado BRASIL')
    if idade >= 21:
        print('Liberado EUA e BRASIL')
    if idade == 1:
        print('Não está liberado')