def classifica_idade(idade):
    if idade<12:
        print('crianca')
    elif  12<=idade<18:
        print('adolescente')
    else:
        print('adulto')
    return classifica_idade
idade = int(input('Qual a sua idade?'))