def verifica_idade(i):
    if i<18:
        print('Não está liberado')
    elif i=>21:
        print('Liberado EUA e Brasil')
    else i>17:
        print('Liberado Brasil')
    return i