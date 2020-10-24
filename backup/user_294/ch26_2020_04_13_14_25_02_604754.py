casa = float(input("valor da casa: "))
salario = float(input('valor do salario: '))
anos= int(input('quantidade de anos: '))
prestacao = int(casa/(anos*12))
if prestacao <= 0.3*salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')