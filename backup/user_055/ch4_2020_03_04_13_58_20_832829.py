def classifica_idade(idade):
    idade = int(input('idade: '))
    return idade

idade = int(input('idade: '))
if idade <= 11:
    print('crianca')
if 11 > idade or idade < 18:
    print('adolescente')
if idade >= 18:
    print('adulto')
                       
    