casa = float(input('Insira o valor da casa: '))
salario = float(input('Insira o valor do salário: '))
anos = int(input('Insira a quantidade de anos: '))

prestacao = casa/(anos*12)

if prestacao > salario * 0.30:
    print('Empréstimo não aprovado')

else:
    print('Empréstimo aprovado')