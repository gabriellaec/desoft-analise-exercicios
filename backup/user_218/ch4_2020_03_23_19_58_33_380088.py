a = input('Digite a sua idade: ')
idade = int (a)
if idade <= 11:
    print('crianca')
elif idade >= 12 and idade <=17:
    print('adolescente')
elif idade >= 18:
    print('adulto')