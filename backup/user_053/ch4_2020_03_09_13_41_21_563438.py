def classifica_idade(idade):
    x=idade
    return x

a=int(input('Digite a sua idade: '))
b=classifica_idade(a)

if b<=11:
    print('crianca')
elif b>11 and b<=17:
    print('adolescente')
else:
    print('adulto')