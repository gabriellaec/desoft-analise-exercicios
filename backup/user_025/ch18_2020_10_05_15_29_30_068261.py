def verifica_idade(a):
    if a >= 21:
        print('Liberado EUA e BRASIL')
    elif a >= 18:
        print('Liberado BRASIL')
    else:
        print('Não está liberado')