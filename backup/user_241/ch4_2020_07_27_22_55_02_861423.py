def classifica_idade(idade):
    idade = int
    if idade <= 11:
        print('crianca')
    elif 11 < idade <= 17:
        print('adolescente')
    elif idade >= 18:
        print('adulto')
    