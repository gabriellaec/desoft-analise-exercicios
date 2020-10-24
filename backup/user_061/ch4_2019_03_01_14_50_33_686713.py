def classifica_idade(idade):
    if idade > 0:
        if idade < 12:
            print('crianca')
        elif idade < 18:
            print('adolescente')
        else:
            print('adulto')
        