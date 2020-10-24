def verifica_idade(idade):
    if idade>=21:
        print('Liberado EUA e BRASIL')
    elif 17<idade<21:
        print('Liberado BRASIL')
    else:
        print('Não está liberado')
