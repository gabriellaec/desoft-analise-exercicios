casa = float(input('Digite o valor da casa? R$: '))
salario = float(input('Digite o valor do seu salario? R$: '))
anos = int(input('Deseja pagar em quantos anos? '))
prestação = (casa / (anos * 12))
minimo = salario * 30 / 100

if prestação > minimo:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
