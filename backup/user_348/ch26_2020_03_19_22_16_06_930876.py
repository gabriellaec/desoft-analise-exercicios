casa = float(input('valor da casa:'))
salário = float(input('valor do salário:'))
anos = int(input('quantidade de anos:'))
prestação = int(casa/(anos*12))
if prestação <= 0.3*salário:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')