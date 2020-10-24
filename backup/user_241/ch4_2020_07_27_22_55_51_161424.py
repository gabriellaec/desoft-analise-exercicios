def classifica_idade(idade):
    x = int(idade)
    if x <= 11:
        print('crianca')
    elif 11 < x <= 17:
        print('adolescente')
    elif x >= 18:
        print('adulto')
    