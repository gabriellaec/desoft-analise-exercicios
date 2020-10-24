casa= float(input('Valor da casa: '))
salario = float(input('Seu salario: '))
ano= int(input('Por quantos anos: '))
meses= ano * 12
prestacao = casa / meses
if prestacao > salario * 0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')