def verifica_idade(idade):
    if int(idade) >= 21:
        print('Liberado EUA e BRASIL')
    elif 18 <= int(idade) < 21:
        print('Liberado BRASIL')
    else:
        print('Não está liberado')