casa = float(input(''))
salario = float(input(''))
anos = float(input(''))
prestação = (casa / (anos * 12))
minimo = salario * 30 / 100

if prestação > minimo:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
