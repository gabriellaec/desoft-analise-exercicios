# classifica_idade = input('Qual sua idade?')
def classifica_idade(idade):
    x = int(input(idade)):
    if idade <= 11:
        print('crianca')
    elif idade >= 12 and idade <= 17:
        print('adolescente')
    else:
        print('adulto')