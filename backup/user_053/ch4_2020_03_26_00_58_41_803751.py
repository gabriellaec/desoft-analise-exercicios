def classifica_idade(idade):
    x=idade
    if x<12:
        print('crianca')
    elif x>11 and x<18:
        print('adolescente')
    else:
        print('adulto')
    return x

a=int(input('Digite sua idade: '))
b=classifica_idade(a)