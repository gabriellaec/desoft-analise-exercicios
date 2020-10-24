def classifica_idade(idade):
    x=idade
    if x<12:
        print('crianca')
    elif x>11 and x<17:
        print('adolescente')
    else:
        print('adulto')
    return x

a=5
b=classifica_idade(a)