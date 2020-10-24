def verifica_idade(idade):
    if idade >= 18 and idade <= 21:
        print('Liberado BRASIL')
    if idade > 21:
        print('Liberado EUA e BRASIL')
    else:
        if idade < 18:
            print('Não está liberado')