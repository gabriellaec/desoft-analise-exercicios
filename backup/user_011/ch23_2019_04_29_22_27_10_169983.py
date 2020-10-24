def verifica_idade(idade):
    if idade>=22:
        print('Liberado EUA e BRASIL')
    elif 17<idade<22:
        print('Liberado BRASIL')
    else:
        print('Não está liberado')
    return verifica_idade


