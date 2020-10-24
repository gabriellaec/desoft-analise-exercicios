def verifica_idade(idade):
    if idade >= 21:
        print('Liberado nos EUA e BRASIL')
    elif idade >= 18 and idade < 21:
        print('Liberado no BRASIL')
    else:
        print('Não está liberado')
    return idade

    