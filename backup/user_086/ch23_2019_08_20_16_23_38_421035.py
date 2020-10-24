def verifica_idade(idade):
    if idade>=21:
        print('Liberado EUA e BRASIL')
    if idade<18:
        print('Não está liberado')
    else:
        print('Liberado BRASIL')